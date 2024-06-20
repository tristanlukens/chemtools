import re
from helpers.parsing import subcommand, subcommand_arguments

# TODO: add (recursive) functionality for (nested) polyatomic ions
# TODO: add support for complex ions (with [])

weights = {"H": 1.008, "C": 12.01, "O": 16.00}

split_regex = r"[A-Z][a-z]*\d*|\(.*\)\d*"
split = lambda molecule: re.findall(split_regex, molecule)

filter_polyatomic_ions = lambda splits: filter(lambda split: "(" in split, splits)


def _process_polyatomic_ions(splits):
    polies = filter_polyatomic_ions(splits)
    if len(polies) > 0:
        _process_polyatomic_ions(polies)
    return polies


def _action(args):
    molecule = args.molecule
    print(molecule)

    splits = split(molecule)
    polyatomic_ions = list(filter(filter_polyatomic_ions, splits))
    print(polyatomic_ions)


@subcommand([subcommand_arguments("molecule", help="Molecule/element")])
def molar_weight(args):
    """
    Calculates the molar weight of the supplied molecule/element.

    Example input: `C2H5OH`, `Fe(OH)2`.  Note that the correctness of the molecule will
    not be checked. Use `check` for this functionality.
    """

    _action(args)
