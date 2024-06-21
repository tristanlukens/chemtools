import re
from helpers.parsing import subcommand, subcommand_arguments
from helpers.periodic_table import periodic_table

from dataclasses import dataclass

# TODO: add (recursive) functionality for (nested) polyatomic ions
# TODO: add support for complex ions (with [])


def _split(molecule):
    """
    Split molecule into its parts: `Fe(OH)2` &rarr; `[Fe, (OH)2]`; `C2H5OH` &rarr; `[C2, H5, O, H]`
    """

    # Match 1) one uppercase, followed by 0 or more lowercase characters,
    # followed by zero or more numbers or match 2) anything surrounded by
    # parentheses followed by zero or more numbers
    split_regex = re.compile(r"[A-Z][a-z]*\d*|\(.*\)\d*")
    return re.findall(split_regex, molecule)


@dataclass
class _Element:
    """
    Element dataclass. Takes the element's symbol, and an integer amount.
    """

    symbol: str
    amount: int


def _to_dict(element, elements):
    """
    Populates the `elements` dict with elements. When they don't have a value (&rarr; `Fe` is denoted
    `Fe`, not `Fe1`), `amount = 1` is assumed. The `elements` array is then populated according to
    existing values.
    """


split_in_elements = lambda m: re.findall(r"([A-Z][a-z]*)(\d*)", m)


def _process_part(part, elements):
    if "(" in part:
        # The factor with which you multiple the rest of the coefficients
        # will always be the last character in the part
        factor = part[-1]

    split_in_elements = re.findall(r"([A-z][a-z]*)(\d*)", part)
    print(split_in_elements)

    for element in split_in_elements:
        element = _Element(*element)
        element.amount = 1 if element.amount == "" else int(element.amount)
        elements[element.symbol] = elements.get(element.symbol, 0) + element.amount


def _action(args):
    molecule = args.molecule

    parts = _split(molecule)
    print(parts)

    elements = {}

    for part in parts:
        _process_part(part, elements)

    # print(elements)


@subcommand([subcommand_arguments("molecule", help="Molecule/element")])
def molar_weight(args):
    """
    Calculates the molar weight of the supplied molecule/element.

    Example input: `C2H5OH`, `Fe(OH)2`.  Note that the correctness of the molecule will
    not be checked.
    """

    _action(args)
