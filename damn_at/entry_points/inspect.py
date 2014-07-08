"""
Inspect
=======

Entry point for inspecting a file.
"""
# Standard
import os
import sys

# Damn
from damn_at import MetaDataStore
from damn_at.entry_points import EntryPoint
from damn_at.utilities import pretty_print_file_description


class InspectAsset(EntryPoint):
    """Inspect an assets metadata."""

    help_text = '$ damn inspect INPUT_FILE'
    name = 'inspect'
    min_args = 1
    max_args = 1

    def command(self, *args, **options):
        """Extract xml from a given document and output as a seperate file"""
        input_file = args[0]

        if not os.path.exists(input_file):
            self.error('Could not find file %s. Please check your filename and'
                       ' path.' % input_file)

        file_path = os.path.abspath(input_file)
        m = MetaDataStore(os.path.dirname(file_path))
        file_descr = m.get_metadata('', os.path.basename(file_path))

        # Print the output
        self.show_description()
        self.std_out('Inspecting "%s"\n' % self.green(file_path))
        pretty_print_file_description(file_descr)

        sys.exit(0)
