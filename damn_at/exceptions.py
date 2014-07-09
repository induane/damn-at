"""
Exceptions
==========

Custom exceptions for damn_at project
"""


class TranscoderException(Exception):
    """Base Transcoder Exception"""
    def __init__(self, msg):
        Exception.__init__(self)
        self.msg = msg

    def __str__(self):
        return repr(self.msg)


class TranscoderFileException(TranscoderException):
    """Something wrong with the file"""
    pass


class TranscoderUnknownTypeException(TranscoderException):
    """Unknown type"""
    pass


class TranscoderUnknownAssetException(TranscoderException):
    """Unknown asset"""
    pass
