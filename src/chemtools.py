import lib.molar_weight
import lib.pH

from helpers.parsing import main_parser

# Credit to https://mike.depalatis.net/blog/simplifying-argparse.html for the
# code in the main function


def main():
    args = main_parser.parse_args()
    if args.subcommand is None:
        main_parser.print_help()
    else:
        args.func(args)


if __name__ == "__main__":
    main()
