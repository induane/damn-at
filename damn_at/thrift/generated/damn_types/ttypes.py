#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class MetaDataType:
  BOOL = 1
  INT = 2
  DOUBLE = 3
  STRING = 4

  _VALUES_TO_NAMES = {
    1: "BOOL",
    2: "INT",
    3: "DOUBLE",
    4: "STRING",
  }

  _NAMES_TO_VALUES = {
    "BOOL": 1,
    "INT": 2,
    "DOUBLE": 3,
    "STRING": 4,
  }


class MetaDataValue:
  """
  Attributes:
   - type
   - bool_value
   - int_value
   - double_value
   - string_value
  """

  thrift_spec = (
    None, # 0
    (1, TType.I32, 'type', None, None, ), # 1
    (2, TType.BOOL, 'bool_value', None, None, ), # 2
    (3, TType.I64, 'int_value', None, None, ), # 3
    (4, TType.DOUBLE, 'double_value', None, None, ), # 4
    (5, TType.STRING, 'string_value', None, None, ), # 5
  )

  def __init__(self, type=None, bool_value=None, int_value=None, double_value=None, string_value=None,):
    self.type = type
    self.bool_value = bool_value
    self.int_value = int_value
    self.double_value = double_value
    self.string_value = string_value

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.I32:
          self.type = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BOOL:
          self.bool_value = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.int_value = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.DOUBLE:
          self.double_value = iprot.readDouble();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.string_value = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('MetaDataValue')
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.I32, 1)
      oprot.writeI32(self.type)
      oprot.writeFieldEnd()
    if self.bool_value is not None:
      oprot.writeFieldBegin('bool_value', TType.BOOL, 2)
      oprot.writeBool(self.bool_value)
      oprot.writeFieldEnd()
    if self.int_value is not None:
      oprot.writeFieldBegin('int_value', TType.I64, 3)
      oprot.writeI64(self.int_value)
      oprot.writeFieldEnd()
    if self.double_value is not None:
      oprot.writeFieldBegin('double_value', TType.DOUBLE, 4)
      oprot.writeDouble(self.double_value)
      oprot.writeFieldEnd()
    if self.string_value is not None:
      oprot.writeFieldBegin('string_value', TType.STRING, 5)
      oprot.writeString(self.string_value)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TargetMimetypeOption:
  """
  Attributes:
   - name
   - type
   - constraint
   - default_value
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'name', None, None, ), # 1
    (2, TType.STRING, 'type', None, None, ), # 2
    (3, TType.STRING, 'constraint', None, None, ), # 3
    (4, TType.STRING, 'default_value', None, None, ), # 4
  )

  def __init__(self, name=None, type=None, constraint=None, default_value=None,):
    self.name = name
    self.type = type
    self.constraint = constraint
    self.default_value = default_value

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.name = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.type = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRING:
          self.constraint = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.STRING:
          self.default_value = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TargetMimetypeOption')
    if self.name is not None:
      oprot.writeFieldBegin('name', TType.STRING, 1)
      oprot.writeString(self.name)
      oprot.writeFieldEnd()
    if self.type is not None:
      oprot.writeFieldBegin('type', TType.STRING, 2)
      oprot.writeString(self.type)
      oprot.writeFieldEnd()
    if self.constraint is not None:
      oprot.writeFieldBegin('constraint', TType.STRING, 3)
      oprot.writeString(self.constraint)
      oprot.writeFieldEnd()
    if self.default_value is not None:
      oprot.writeFieldBegin('default_value', TType.STRING, 4)
      oprot.writeString(self.default_value)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TargetMimetype:
  """
  Attributes:
   - mimetype
   - template
   - options
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'mimetype', None, None, ), # 1
    (2, TType.STRING, 'template', None, None, ), # 2
    (3, TType.LIST, 'options', (TType.STRUCT,(TargetMimetypeOption, TargetMimetypeOption.thrift_spec)), None, ), # 3
  )

  def __init__(self, mimetype=None, template=None, options=None,):
    self.mimetype = mimetype
    self.template = template
    self.options = options

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.mimetype = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.template = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.options = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = TargetMimetypeOption()
            _elem5.read(iprot)
            self.options.append(_elem5)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TargetMimetype')
    if self.mimetype is not None:
      oprot.writeFieldBegin('mimetype', TType.STRING, 1)
      oprot.writeString(self.mimetype)
      oprot.writeFieldEnd()
    if self.template is not None:
      oprot.writeFieldBegin('template', TType.STRING, 2)
      oprot.writeString(self.template)
      oprot.writeFieldEnd()
    if self.options is not None:
      oprot.writeFieldBegin('options', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.options))
      for iter6 in self.options:
        iter6.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class File:
  """
  Attributes:
   - filename
   - data
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'filename', None, None, ), # 1
    (2, TType.STRING, 'data', None, None, ), # 2
  )

  def __init__(self, filename=None, data=None,):
    self.filename = filename
    self.data = data

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.filename = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.data = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('File')
    if self.filename is not None:
      oprot.writeFieldBegin('filename', TType.STRING, 1)
      oprot.writeString(self.filename)
      oprot.writeFieldEnd()
    if self.data is not None:
      oprot.writeFieldBegin('data', TType.STRING, 2)
      oprot.writeString(self.data)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class FileId:
  """
  Attributes:
   - filename
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'filename', None, None, ), # 1
  )

  def __init__(self, filename=None,):
    self.filename = filename

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.filename = iprot.readString();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('FileId')
    if self.filename is not None:
      oprot.writeFieldBegin('filename', TType.STRING, 1)
      oprot.writeString(self.filename)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AssetId:
  """
  Attributes:
   - subname
   - mimetype
   - file
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'subname', None, None, ), # 1
    (2, TType.STRING, 'mimetype', None, None, ), # 2
    (3, TType.STRUCT, 'file', (FileId, FileId.thrift_spec), None, ), # 3
  )

  def __init__(self, subname=None, mimetype=None, file=None,):
    self.subname = subname
    self.mimetype = mimetype
    self.file = file

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.subname = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.mimetype = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.STRUCT:
          self.file = FileId()
          self.file.read(iprot)
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AssetId')
    if self.subname is not None:
      oprot.writeFieldBegin('subname', TType.STRING, 1)
      oprot.writeString(self.subname)
      oprot.writeFieldEnd()
    if self.mimetype is not None:
      oprot.writeFieldBegin('mimetype', TType.STRING, 2)
      oprot.writeString(self.mimetype)
      oprot.writeFieldEnd()
    if self.file is not None:
      oprot.writeFieldBegin('file', TType.STRUCT, 3)
      self.file.write(oprot)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class AssetReference:
  """
  Attributes:
   - asset
   - metadata
   - dependencies
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'asset', (AssetId, AssetId.thrift_spec), None, ), # 1
    (2, TType.MAP, 'metadata', (TType.STRING,None,TType.STRUCT,(MetaDataValue, MetaDataValue.thrift_spec)), None, ), # 2
    (3, TType.LIST, 'dependencies', (TType.STRUCT,(AssetId, AssetId.thrift_spec)), None, ), # 3
  )

  def __init__(self, asset=None, metadata=None, dependencies=None,):
    self.asset = asset
    self.metadata = metadata
    self.dependencies = dependencies

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.asset = AssetId()
          self.asset.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.MAP:
          self.metadata = {}
          (_ktype8, _vtype9, _size7 ) = iprot.readMapBegin() 
          for _i11 in xrange(_size7):
            _key12 = iprot.readString();
            _val13 = MetaDataValue()
            _val13.read(iprot)
            self.metadata[_key12] = _val13
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.dependencies = []
          (_etype17, _size14) = iprot.readListBegin()
          for _i18 in xrange(_size14):
            _elem19 = AssetId()
            _elem19.read(iprot)
            self.dependencies.append(_elem19)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('AssetReference')
    if self.asset is not None:
      oprot.writeFieldBegin('asset', TType.STRUCT, 1)
      self.asset.write(oprot)
      oprot.writeFieldEnd()
    if self.metadata is not None:
      oprot.writeFieldBegin('metadata', TType.MAP, 2)
      oprot.writeMapBegin(TType.STRING, TType.STRUCT, len(self.metadata))
      for kiter20,viter21 in self.metadata.items():
        oprot.writeString(kiter20)
        viter21.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.dependencies is not None:
      oprot.writeFieldBegin('dependencies', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.dependencies))
      for iter22 in self.dependencies:
        iter22.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class FileReference:
  """
  Attributes:
   - file
   - hash
   - assets
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'file', (FileId, FileId.thrift_spec), None, ), # 1
    (2, TType.STRING, 'hash', None, None, ), # 2
    (3, TType.LIST, 'assets', (TType.STRUCT,(AssetReference, AssetReference.thrift_spec)), None, ), # 3
  )

  def __init__(self, file=None, hash=None, assets=None,):
    self.file = file
    self.hash = hash
    self.assets = assets

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.file = FileId()
          self.file.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.STRING:
          self.hash = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.assets = []
          (_etype26, _size23) = iprot.readListBegin()
          for _i27 in xrange(_size23):
            _elem28 = AssetReference()
            _elem28.read(iprot)
            self.assets.append(_elem28)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('FileReference')
    if self.file is not None:
      oprot.writeFieldBegin('file', TType.STRUCT, 1)
      self.file.write(oprot)
      oprot.writeFieldEnd()
    if self.hash is not None:
      oprot.writeFieldBegin('hash', TType.STRING, 2)
      oprot.writeString(self.hash)
      oprot.writeFieldEnd()
    if self.assets is not None:
      oprot.writeFieldBegin('assets', TType.LIST, 3)
      oprot.writeListBegin(TType.STRUCT, len(self.assets))
      for iter29 in self.assets:
        iter29.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)