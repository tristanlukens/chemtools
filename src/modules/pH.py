from helpers.parsing import subcommand, subcommand_arguments

import math


def _pH_action(args):
    # Anonymous function to quickly calculate pH (or pOH) from hydronium (or hydroxide) concentration
    calculate = lambda c: -1 * math.log(c, 10)

    concentration = (
        float(args.concentration) / 1000 if args.milli else float(args.concentration)
    )

    decimals = int(args.decimals)

    if args.hydroxide:
        pOH = calculate(concentration)
        return round(14 - pOH, decimals)

    return round(calculate(concentration), decimals)


@subcommand(
    [
        subcommand_arguments("concentration", help="Hydronium concentration"),
        subcommand_arguments(
            "-m",
            "--milli",
            dest="milli",
            help="Use millimolars instead of molars",
            action="store_true",
        ),
        subcommand_arguments(
            "--hydroxide",
            dest="hydroxide",
            help="Use hydroxide concentration instead of hydronium",
            action="store_true",
        ),
        subcommand_arguments(
            "-d",
            "--decimals",
            dest="decimals",
            help="Number of decimals in pH",
            default=2,
        ),
    ]
)
def pH(args):
    """
    Calculate the pH of an aqeous solution with the supplied molarity of hydronium ions.

    Example input: `3.2`, `-m --hydroxide 1.79`
    """

    print(_pH_action(args))
