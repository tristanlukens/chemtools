import lib.pH
import lib.molar_weight

from helpers.parsing import main_parser


if __name__ == "__main__":
    args = main_parser.parse_args()
    if args.subcommand is None:
        main_parser.print_help()
    else:
        args.func(args)
