"""
Assimp-based analyzer.
"""
import os
import subprocess

from pyassimp.pyassimp import *

from damn_at import logger
from damn_at.analyzer import AnalyzerException

from damn_at import mimetypes
from damn_at import MetaDataType, MetaDataValue
from damn_at import FileId, FileDescription, AssetDescription, AssetId

from damn_at.pluginmanager import IAnalyzer

#TODO: not exactly reliable, a lot of unknown mimetypes for those extensions :/
def get_assimp_types():
    """
    Extract all possible formats and store their mime types
    """
    try:
        pro = subprocess.Popen(['assimp', 'listext'], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        out, err = pro.communicate()
        if pro.returncode != 0:
            logger.debug("'assimp listext' failed with error code %d! "%(pro.returncode),
                    out, err)
            return []
    except OSError as oserror:
        logger.debug("'assimp listext' failed! %s", oserror)
        return []

    extensions = out.split(';')
    mimes = []
    for ext in extensions:
        mime = mimetypes.guess_type('file.'+ext, False)[0]
        print ext, mime
        mimes.append(mime)
    return mimes


class AssimpAnalyzer(IAnalyzer):
    """Assimp-based analyzer."""
    handled_types = ['application/wavefront-obj']

    def __init__(self):
        IAnalyzer.__init__(self)

    def activate(self):
        pass

    def analyze(self, an_uri):
        fileid = FileId(filename = os.path.abspath(an_uri))
        file_descr = FileDescription(file = fileid)
        file_descr.assets = []

        assimp_mimetype = 'application/assimp'

        scene = None
        try:
            scene = load(an_uri)

            textures = {}
            materials = {}

            from damn_at.analyzers.mesh.metadata import MetaDataAssimpTexture, MetaDataAssimpMesh, MetaDataAssimpMaterial

            for i, texture in enumerate(scene.textures):
                name = texture.mName.data if texture.mName and texture.mName.data else 'texture-'+str(i)
                asset_descr = AssetDescription(asset = AssetId(subname = name, mimetype = assimp_mimetype+".texture", file = fileid))
                asset_descr.metadata = MetaDataAssimpTexture.extract(texture)
                file_descr.assets.append(asset_descr)
                textures[i] = asset_descr

            for i, material in enumerate(scene.materials):
                properties = GetMaterialProperties(material)
                name = properties.get('?mat.name', 'material-'+str(i))
                asset_descr = AssetDescription(asset = AssetId(subname = name, mimetype = assimp_mimetype+".material", file = fileid))
                asset_descr.metadata = MetaDataAssimpMaterial.extract(properties)
                file_descr.assets.append(asset_descr)
                materials[i] = asset_descr

            for i, mesh in enumerate(scene.meshes):
                name = mesh.mName.data if mesh.mName and mesh.mName.data else 'mesh-'+str(i)
                asset_descr = AssetDescription(asset = AssetId(subname = name, mimetype = assimp_mimetype+".mesh", file = fileid))
                asset_descr.metadata = MetaDataAssimpMesh.extract(mesh)
                asset_descr.dependencies = []
                #Dependencies
                if mesh.mMaterialIndex is not None:
                    if mesh.mMaterialIndex in materials:
                        asset_descr.dependencies.append(materials[mesh.mMaterialIndex].asset)
                file_descr.assets.append(asset_descr)

        finally:
            release(scene)

        '''
        obj = Loader(an_uri)

        from damn_at.analyzers.mesh.metadata import MetaDataWaveFrontDefault, MetaDataWaveFrontGroup

        d_asset_descr = AssetDescription(asset = AssetId(subname = 'default', mimetype = "application/wavefront-obj", file = fileid))
        d_asset_descr.metadata = MetaDataWaveFrontDefault.extract(obj)
        file_descr.assets.append(d_asset_descr)


        for name, group in obj.groups.items():
            if name != 'default':
                asset_descr = AssetDescription(asset = AssetId(subname = name, mimetype = "application/wavefront-obj.group", file = fileid))
                asset_descr.metadata = MetaDataWaveFrontGroup.extract(group)
                asset_descr.dependencies = [d_asset_descr.asset]
                file_descr.assets.append(asset_descr)
        '''

        return file_descr


class Loader(object):
    def __init__(self, path):
        vertices = []
        normals = []
        texcoords = []
        default = {'faces': []}
        current = default
        self.groups = {'default': default}
        for line in open(path, "r"):
          if line.startswith('#'): continue
          values = line.split()
          if not values: continue
          if values[0] == 'g':
            current = {'faces': []}
            group_name = values[1]
            print 'Group', group_name, values
            self.groups[group_name] = current
          elif values[0] == 'v':
            vertices.append(tuple(map(float, values[1:4])))
          elif values[0] == 'vn':
            normals.append(tuple(map(float, values[1:4])))
          elif values[0] == 'vt':
            texcoords.append(tuple(map(float, values[1:3])))
          elif values[0] == 's':
            current['smooth'] = bool(values[2:3])
          elif values[0] == 'f':
            faces = current['faces']
            face = []
            for v in values[1:]:
                w = map(lambda x: int(x) if x else None, v.split('/'))
                w = map(lambda x: x-1 if x != None and x > 0 else x, w)
                face.append(tuple(w))
            faces.append(tuple(face))
          else:
              print 'Loader, value not known', values[0], line
        # save result
        self.vertices = vertices
        self.normals = normals
        self.texcoords = texcoords
