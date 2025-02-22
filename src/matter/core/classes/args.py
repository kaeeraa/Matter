"""This module contains the argument parser for the bot."""

from argparse import ArgumentParser


class Args:
    """Argument parser for the bot."""
    _parser = ArgumentParser(
        prog="Matter bot",
        description="An all-in-one ticket bot for Discord.",
        epilog="https://github.com/kaeeraa/Matter",
    )

    def __init__(self) -> None:
        self._parser.add_argument(
            "-v", "--verbose",
            action="store_true",
            help="Enable verbose logging",
            default=False
        )
        self._parser.add_argument(
            "-vv", "--vomit",
            action="store_true",
            help="Enable trace (vomit) logging",
            default=False
        )

    @property
    def args(self) -> object:
        """Parse the command line arguments."""
        return self._parser.parse_args()


args = Args().args
