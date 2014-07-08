"""
Common
======

Common functions to be used by various entry points.
"""
# Standard
from os.path import exists
from os.path import abspath


def vararg_callback(option, opt_str, value, parser):
    """
    Custom callback for arbitrary length arguments blatantly taken from
    pythons documentation at: http://docs.python.org/2/library/optparse.html
    Under the headline: 15.5.4.9. Callback example 6: variable arguments
    """
    assert value is None
    value = []

    def floatable(str_val):
        """
        Small function used to determine whether or not a string value
        could be parsed into a float

        :type str_val: string
        :param str_val: value to attempt to cast as float
        :returns: True or False determination of whether a value can be a float
        :rtype: bool
        """
        try:
            float(str_val)
            return True
        except ValueError:
            return False

    for arg in parser.rargs:
        # stop on --foo like options
        if arg[:2] == "--" and len(arg) > 2:
            break
        # stop on -a, but not on -3 or -3.0
        if arg[:1] == "-" and len(arg) > 1 and not floatable(arg):
            break
        value.append(arg)

    del parser.rargs[:len(value)]
    if opt_str == '--files':
        for val in value:
            if not exists(abspath(val)):
                print (
                    'Warning: %s could not be found. This file may be s'
                    'kipped during processing.' % val
                )
    setattr(parser.values, option.dest, value)
