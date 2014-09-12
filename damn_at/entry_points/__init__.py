"""
Entry Points
============

Base class for entry points to inherit from. Simplifies construction of
options and allows for colorized outputs.
"""

# Standard
import sys
import traceback
import contextlib
from StringIO import StringIO
from argparse import ArgumentParser
CMD_DESCRIPTION = r'''
 ___   _   __  __ _  _
|   \ /_\ |  \/  | \| |
| |) / _ \| |\/| | .` |
|___/_/ \_\_|  |_|_|\_|
    Digital Assets Managed Neatly.
'''


@contextlib.contextmanager
def outputIO():
    """
    Context manager that replaces standard out and standard error with a single
    file like object. This is useful for suppressing writes to stderr or stdout
    that cannot be suppressed by normal means
    """

    old_out = sys.stdout
    old_err = sys.stderr

    # Create a file-like object to catch output
    out_flo = StringIO()

    # Map standard out and standard error to this file like object
    sys.stdout = out_flo
    sys.stderr = out_flo

    yield out_flo

    # Reset stdout and stderr to original settings
    sys.stdout = old_out
    sys.stderr = old_err


class Option(object):
    """
    Uber Basic class for storing arguments for ArgumentParser
    """
    def __init__(self, *args, **options):
        self.args = args
        self.options = options


class EntryPoint(object):
    """
    Base class for entry points to inherit from. You'll need to implement your
    own option list for parsed options. The method 'command' will automatically
    be run with whatever options come from OptParse.
    """

    # Command line options - these should be overloaded by subclasses
    option_list = []
    help_text = ''
    epilog = ''
    name = 'base_command'
    min_args = 0  # If minimum arguments is not met a help message is displayed
    max_args = False  # Specify maximum arg count. False means no limit.
    clear_console = False  # Set to true to clear the screen before command

    # Console color definitions
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    def __init__(self, *args, **kwargs):
        """Setup the basic command and run automated methods"""
        if self.clear_console:
            self.clear_screen()

        self.parser = self.create_parser()
        super(EntryPoint, self).__init__()

        # Call command runner.
        self._run_command()

    def __exit__(self, *args, **kwargs):
        pass

    def __enter__(self, *args, **kwargs):
        return self

    @staticmethod
    def option(*args, **kwargs):
        """
        Create an instance of the options class from the given args
        """
        return Option(*args, **kwargs)

    def create_parser(self):
        """
        Create and return an "ArgumentParser" which will be used to parse the
        arguments to this command.
        """
        parser = ArgumentParser(
            prog="damn",
            usage=self.green(self.help_text),
            epilog=self.green(self.epilog)
        )
        for item in self.option_list:
            parser.add_argument(*item.args, **item.options)
        return parser

    def help(self, exit=True):
        """
        Prints help text to standard out and by default, exits.

        :type exit: bool
        :param exit: flag to exit to console. Defaults to True
        """
        self.std_out(self.help_text, exit=exit)

    @staticmethod
    def clear_screen():
        """Clear the console in a hacky way"""
        sys.stdout.write('\x1b[2J\x1b[H')

    def _verify_args(self, arguments):
        """
        Verify that the number of arguments passed matches the requirements
        specified. If an incorrect number of arguments are specified, print
        the usage help text and exit with an error status of -1

        :type arguments: list | tuple
        :param arguments: list of arguments to check the count of
        """
        arglen = len(arguments)

        # Verify arguments
        if self.max_args is False:
            bad_args = (arglen < self.min_args)
        else:
            bad_args = (arglen < self.min_args or arglen > self.max_args)
        if bad_args:
            self.warning("This command requires at least %s "
                         "arguments but only %s %s found." % (
                             self.min_args,
                             len(arguments),
                             "was" if len(arguments) == 1 else "were"
                         ))
            self.green_out("\nUsage:")
            self.help(exit=False)
            sys.exit(-1)

    def _run_command(self):
        """
        Run the command method using the arguments provided from the command
        parser.

        :type show_traceback: bool
        :param show_traceback: display a traceback when an error is detected
        """
        # from argparse import ArgumentError
        # from argparse import ArgumentTypeError
        # Get options from command parser
        self.green_out('Getting args...')

        run_error = False
        with outputIO as output:
            try:
                (options, arguments) = self.parser.parse_known_args()
            except SystemExit:
                run_error = True
            except:
                run_error = True

        if run_error:
            self.error_command()
            sys.exit(-1)

        # try:
        #     (options, arguments) = self.parser.parse_known_args()
        # except ArgumentError as ex:
        #     print("Error: %s" % str(ex))
        #     sys.exit(-1)
        #     self.error_command()
        #     sys.exit(-1)
        # except ArgumentTypeError:
        #     print("Other type error")
        #     sys.exit(-1)
        # except:
        #     print('except??')
        #     sys.exit(-1)
        # self.green_out('Got arguments.')

        # Strip subcommand from arguments list
        base_args = arguments[1:]

        # Verify the arguments are valid. This autoexits on bad input.
        self.green_out('Checking args!')
        self._verify_args(base_args)
        self.green_out('Args validated!!!!')

        try:
            self.command(*base_args, **vars(options))
        except Exception as ex:
            # Get Traceback
            tb = "".join(traceback.format_exception(sys.exc_info()[0],
                                                    sys.exc_info()[1],
                                                    sys.exc_info()[2]))

            self.error("Error running command %s.\n%s\n%s" % (
                self.name,
                ex,
                'Traceback:\n%s' % tb if tb else ''
            ))

    def error_command(self):
        """
        Called when an error occurs when parsing options. By default prints
        a simple error including usage text and exits, but can be overloaded.
        """
        # Get Traceback
        tb = "".join(traceback.format_exception(
            sys.exc_info()[0],
            sys.exc_info()[1],
            sys.exc_info()[2]
        ))
        self.error("Error running error command %s.\n%s" % (
            self.name,
            'Traceback:\n%s' % tb if tb else ''
        ))
        sys.exit(-1)

    def command(self, *arguments, **options):
        """
        No command method error
        """
        header = "Damn:"
        message = (
            "No command method is implemented for this entry point.\nArguments"
            " passed: %s\nKeyword Arguments: %s" % (", ".join(arguments),
                                                    options)
        )
        self.header(header)
        self.error(message)

    def std_out(self, text, exit=False):
        """
        Write a message to standard out and then flush to make sure it is
        written to the console. Alternatively exit the program if exit is set
        to True. Exit code will be 0

        :type text: str
        :param text: message to print to stdout before exiting
        :type exit: bool
        :param exit: exit to the console with an exit code of 0
        """
        sys.stdout.write("%s\n" % text)
        sys.stdout.flush()
        if exit:
            sys.exit(0)

    def error(self, text, exit=True, exit_status=-1):
        """
        Write an error message to the console with the error coloring. Exits to
        console with an error status of -1 by default.

        :type text: str
        :param text: message to print to stdout before exiting
        :type exit: bool
        :param exit: exit to the console with an error status
        :type exit_status: int
        :param exit_status: exit code to use when exit is called. Defaults to
            -1 and is ignored if exit flag is set to False
        """
        message = "%s%s%s\n" % (self.FAIL, text, self.ENDC)
        sys.stderr.write(message)
        sys.stderr.flush()
        if exit:
            sys.exit(exit_status)

    def warning(self, text, exit=False):
        """
        Write a message to standard out in a warning orange color and then
        flush to make sure it is written to the console. Alternatively exit the
        program if exit is set to True.

        :type text: str
        :param text: message to print to stdout
        :type exit: bool
        :param exit: exit to the console with an exit code of 0
        """
        self.std_out(self.red(text), exit=exit)

    def green_out(self, text, exit=False):
        """
        Write a message to standard out in a friendly green color and then
        flush to make sure it is written to the console. Alternatively exit the
        program if exit is set to True.

        :type text: str
        :param text: message to print to stdout
        :type exit: bool
        :param exit: exit to the console with an exit code of 0
        """
        self.std_out(self.green(text), exit=exit)

    def blue_out(self, text, exit=False):
        """
        Write a message to standard out in a friendly green color and then
        flush to make sure it is written to the console. Alternatively exit the
        program if exit is set to True.

        :type text: str
        :param text: message to print to stdout
        :type exit: bool
        :param exit: exit to the console with an exit code of 0
        """
        self.std_out(self.blue(text), exit=exit)

    def header(self, text, exit=False):
        """
        Write a message to standard out in a dark purple color that is useful
        for header messages. Flushes std_out to make sure it is written to the
        console and alternatively exit the program if exit is set to True.

        :type text: str
        :param text: message to print to stdout
        :type exit: bool
        :param exit: exit to the console with an exit code of 0
        """
        self.std_out(self.purple(text), exit=exit)

    def red(self, text):
        """
        Wrap text in console color red and return it

        :type text: str
        :param text: string to wrap with color codes
        :returns: augmented string
        :rtype: str
        """
        return "%s%s%s" % (self.WARNING, text, self.ENDC)

    def purple(self, text):
        """
        Wrap text in console color purple and return it

        :type text: str
        :param text: string to wrap with color codes
        :returns: augmented string
        :rtype: str
        """
        return "%s%s%s" % (self.HEADER, text, self.ENDC)

    def blue(self, text):
        """
        Wrap text in console color blue and return it

        :type text: str
        :param text: string to wrap with color codes
        :returns: augmented string
        :rtype: str
        """
        return "%s%s%s" % (self.OKBLUE, text, self.ENDC)

    def green(self, text):
        """
        Wrap text in console color green and return it

        :type text: str
        :param text: string to wrap with color codes
        :returns: augmented string
        :rtype: str
        """
        return "%s%s%s" % (self.OKGREEN, text, self.ENDC)

    def yellow(self, text):
        """
        Wrap text in console color yellow and return it

        :type text: str
        :param text: string to wrap with color codes
        :returns: augmented string
        :rtype: str
        """
        return "%s%s%s" % (self.WARNING, text, self.ENDC)

    def show_description(self):
        """
        Print the application description to the command line.
        """
        self.header(CMD_DESCRIPTION)
