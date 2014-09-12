"""
Transcode
=========

Entry point for transcoding a file.
"""
# Standard
import os
import re
import sys
import logging
from argparse import ArgumentParser

# Damn
from damn_at.transcoder import Transcoder
from damn_at.entry_points import EntryPoint
from damn_at.metadatastore import MetaDataStore

from damn_at.utilities import (
    find_asset_ids_in_file_descr,
    get_asset_names_in_file_descr
)
from damn_at.exceptions import (
    TranscoderUnknownAssetException,
    TranscoderUnknownTypeException
)


class TranscodeAsset(EntryPoint):
    """Inspect an assets metadata."""

    option_list = [
        EntryPoint.option(
            'path',
            help='The path to the FileDescription file'
        ),
        EntryPoint.option(
            'assetname',
            help='The subname of the asset to transcoder'
        ),
        EntryPoint.option(
            'mimetype',
            help='The destination mimetype'
        ),
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
    min_args = 3
    # max_args = 3

    def command(self, *args, **options):
        """Extract xml from a given document and output as a seperate file"""
        logging.basicConfig(format='%(levelname)s:%(message)s',
                            level=options['loglevel'])

        t = Transcoder('/tmp/transcoded/')

        store_path = os.path.dirname(args.path)
        file_name = os.path.basename(args.path)

        m = MetaDataStore(store_path)

        file_descr = m.get_metadata('', file_name)

        regexp = re.compile(r'^(.+?)(\((.+?)\))?$')
        match = regexp.match(args.assetname)

        asset_subname = match.group(1)
        asset_mimetype = match.group(3)

        if asset_subname not in get_asset_names_in_file_descr(file_descr):
            msg = '%s not in file_descr %s' % (
                asset_subname,
                str(get_asset_names_in_file_descr(file_descr))
            )
            raise TranscoderUnknownAssetException(msg)

        asset_ids = find_asset_ids_in_file_descr(file_descr, asset_subname)

        if len(asset_ids) == 1:
            asset_id = asset_ids[0]
        elif asset_mimetype:
            nasset_ids = [asset_id for asset_id in asset_ids if asset_id.mimetype == asset_mimetype]
            if len(nasset_ids) == 1:
                asset_id = nasset_ids[0]
            else:
                assets = ['%s(%s)' % (asset_id.subname, asset_id.mimetype) for asset_id in asset_ids]
                msg = '%s not in file_descr. Please specify one of %s' % (
                    args.assetname,
                    assets
                )
                raise TranscoderUnknownAssetException(msg)
        else:
            mimes = [asset_id.mimetype for asset_id in asset_ids]
            msg = (
                '%s ambigious in file_descr. Please specify "%s(<mimetype>)" w'
                'ith <mimetype> one of %s' % (asset_subname, mimes)
            )
            raise TranscoderUnknownAssetException(msg)

        target_mimetype = t.get_target_mimetype(
            asset_id.mimetype,
            args.mimetype
        )

        if not target_mimetype:
            if asset_id.mimetype not in t.get_target_mimetypes():
                msg = '%s needs to be one of %s' % (
                    asset_id.mimetype,
                    str(t.get_target_mimetypes().keys())
                )
                raise TranscoderUnknownTypeException(msg)
            else:
                targets = [x.mimetype for x in t.get_target_mimetypes()[asset_id.mimetype]]
                msg = '%s needs to be one of %s' % (
                    args.mimetype,
                    str(targets)
                )
                raise TranscoderUnknownTypeException(msg)

        #Process the optional arguments
        parser = ArgumentParser(parents=[self.parser])
        for option in target_mimetype.options:
            help_text = '%s (%s) [default: %s] (%s)' % (
                option.description,
                option.constraint,
                option.default_value,
                option.type
            )
            parser.add_argument(
                "--" + option.name,
                dest=option.name,
                default=option.default_value,
                help=help_text
            )

        updated_options = parser.parse_args()

        # Parse the options using the convert_map of the transcoder
        updated_options = t.parse_options(
            asset_id.mimetype,
            target_mimetype,
            **vars(updated_options)
        )

        self.show_description()
        self.std_out(
            'Transcoding "%s"\n' % self.green(file_descr.file.filename)
        )
        self.std_out('Using: %s' % self.green(target_mimetype.description))
        self.std_out('with: ')
        for option_name, option_value in updated_options.items():
            self.std_out('* %s: %s ' % (option_name, option_value))
        file_paths = t.transcode(
            file_descr,
            asset_id,
            args.mimetype,
            **updated_options
        )
        self.std_out(file_paths)

    def error_command(self):
        """
        Display valid mimetypes and exit.
        """
        self.std_out('BOOGERZ')
        t = Transcoder('')
        for mime, targets in t.get_target_mimetypes().items():
            self.epilog += ' * %s -> %s \n' % (
                mime,
                str(map(lambda x: x.mimetype, targets))
            )
        self.parser.epilog = self.epilog
        self.parser.print_help()
        sys.exit(1)
