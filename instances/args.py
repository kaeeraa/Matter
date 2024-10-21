from argparse import ArgumentParser

parser = ArgumentParser(
    prog="Matter bot",
    description="An all-in-one ticket bot for Discord.",
    epilog="https://github.com/kaeeraa/Matter",
)

parser.add_argument("-V", "--verbose", action="store_true", help="Enable verbose logging", default=False)
parser.add_argument("-VV", "--vomit", action="store_true", help="Enable trace (vomit) logging", default=False)

args = parser.parse_args()
