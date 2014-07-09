"""
Role
====

Transcoder convience class to find the right plugin for a mimetype
and address it.
"""

from damn_at.pluginmanager import DAMNPluginManagerSingleton

from damn_at import (
    TargetMimetype,
    TargetMimetypeOption
)
from damn_at.options import options_to_template, parse_options


class Transcoder(object):
    """
    Analyze files and tries to find known assets types in it.
    """
    def __init__(self, path):
        self._path = path
        self.transcoders = {}
        plugin_mgr = DAMNPluginManagerSingleton.get()

        for plugin in plugin_mgr.getPluginsOfCategory('Transcoder'):
            if plugin.plugin_object.is_activated:
                for src, _ in plugin.plugin_object.convert_map.items():
                    if not src in self.transcoders:
                        self.transcoders[src] = []
                    self.transcoders[src].append(plugin)

        self._build_target_mimetypes()

    def _build_target_mimetypes(self):
        self.target_mimetypes = {}
        self.target_mimetypes_transcoders = {}
        for src_mimetype, transcoders in self.transcoders.items():
            for transcoder in transcoders:
                for dst_mimetype, options in transcoder.plugin_object.convert_map[src_mimetype].items():
                    tmt = TargetMimetype(mimetype=dst_mimetype, description=transcoder.description, template=options_to_template(options))
                    for option in options:
                        tmto = TargetMimetypeOption(name=option.name,
                                                    description=option.description,
                                                    type=option.type_description,
                                                    constraint=option.constraint_description,
                                                    default_value=option.default_description)
                        tmt.options.append(tmto)
                    if not src_mimetype in self.target_mimetypes:
                        self.target_mimetypes[src_mimetype] = []
                        self.target_mimetypes_transcoders[src_mimetype] = []
                    self.target_mimetypes[src_mimetype].append(tmt)
                    self.target_mimetypes_transcoders[src_mimetype].append((tmt, transcoder,))

    def _get_transcoder(self, src_mimetype, target_mimetype):
        """Returns a transcoder

        """
        target_mimetypes = self.target_mimetypes_transcoders[src_mimetype]
        for target, transcoder in target_mimetypes:
            if target == target_mimetype:
                return transcoder

    def get_target_mimetypes(self):
        """
        Returns a list of supported mimetypes, 'handled_types' of all analyzers

        :rtype: map<string, list<TargetMimetype>>
        """
        return self.target_mimetypes

    def get_target_mimetype(self, src_mimetype, mimetype, **options):
        """"""
        # TODO: Need some clever way to select the right transcoder in
        # the list based on options passed.
        if src_mimetype in self.target_mimetypes_transcoders:
            target_mimetypes = self.target_mimetypes_transcoders[src_mimetype]
            for target, transcoder in target_mimetypes:
                if target.mimetype == mimetype:
                    return target

    def parse_options(self, src_mimetype, target_mimetype, **options):
        """"""
        transcoder = self._get_transcoder(src_mimetype, target_mimetype)
        convert_map_entry = transcoder.plugin_object.convert_map[src_mimetype][target_mimetype.mimetype]
        return parse_options(convert_map_entry, **options)

    def get_paths(self, asset_id, target_mimetype, **options):
        """"""
        transcoder = self._get_transcoder(asset_id.mimetype, target_mimetype)
        convert_map_entry = transcoder.plugin_object.convert_map[asset_id.mimetype][target_mimetype.mimetype]

        path_templates = []
        single_options = dict([(option.name, option) for option in convert_map_entry if not option.is_array])
        single_options = dict([(option, value) for option, value in options.items() if option in single_options])
        array_options = dict([(option.name, option) for option in convert_map_entry if option.is_array])
        array_options = dict([(option, value) for option, value in options.items() if option in array_options])

        from damn_at.options import expand_path_template
        path_template = expand_path_template(target_mimetype.template, target_mimetype.mimetype, asset_id, **single_options)

        #TODO: does not work for multiple arrays.
        if len(array_options):
            for key, values in array_options.items():
                from string import Template
                for value in values:
                    t = Template(path_template)
                    file_path = t.safe_substitute(**{key: value})
                    path_templates.append(file_path)
        else:
            path_templates.append(path_template)

        return path_templates

    def transcode(self, file_descr, asset_id, mimetype, **options):
        """
        Transcode the given AssetId in FileDescription to the specified mimetype

        :rtype: list<string> file paths
        """
        target_mimetype = self.get_target_mimetype(asset_id.mimetype, mimetype)
        transcoder = self._get_transcoder(asset_id.mimetype, target_mimetype)

        return transcoder.plugin_object.transcode(self._path, file_descr, asset_id, target_mimetype, **options)
