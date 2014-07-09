"""
Transcode
=========

Entry point for transcoding a file.
"""
# Standard
# import os
import sys
import logging

# Damn
from damn_at.entry_points import EntryPoint


class TranscodeAsset(EntryPoint):
    """Inspect an assets metadata."""

    option_list = [
        EntryPoint.option(
            '-d',
            '--debug',
            action='store_const',
            dest='loglevel',
            const=logging.DEBUG,
            default=logging.WARNING,
            help='Logging Level'
        ),
        EntryPoint.option(
            '-v',
            '--verbose',
            action="store_const",
            dest="loglevel",
            const=logging.INFO,
            help='Be verbose'
        )
    ]
    help_text = '$ damn transcode INPUT_FILE'
    name = 'transcode'
    min_args = 1
    max_args = 1

    def command(self, *args, **options):
        """Extract xml from a given document and output as a seperate file"""
        logging.basicConfig(format='%(levelname)s:%(message)s',
                            level=options['loglevel'])

        self.std_out(str(args))
        self.std_out(str(options))

        sys.exit(0)
