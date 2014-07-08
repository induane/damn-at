"""
Run Damn
========

Entry point for launching Damn services.
"""

# Standard
import sys
import logging

# Damn
from damn_at.entry_points.inspect import InspectAsset


def main():
    """Main entrypoint for command line interface"""
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

    supported_actions = 'inspect'
    try:
        command = sys.argv[1]
    except IndexError:
        print("Missing argument. Supported actions are: %s" % (
            supported_actions
        ))
        sys.exit()

    if command.lower() == 'inspect':
        InspectAsset()
    else:
        print("Unsupported action. Currently supported actions are: %s" % (
            supported_actions
        ))


if __name__ == "__main__":
    main()
