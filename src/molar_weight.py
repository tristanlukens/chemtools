import re

weights = {"H": 1.008, "C": 12.01, "O": 16.00}


# TODO: add (recursive) functionality for (nested) polyatomic ions
# TODO: add support for complex ions (with [])


split_regex = r"[A-Z][a-z]*\d*|\(.*\)\d*"
split = lambda molecule: re.findall(split_regex, molecule)

filter_polyatomic_ions = lambda splits: filter(lambda split: "(" in split, splits)


def process_polyatomic_ions(splits):
    polies = filter_polyatomic_ions(splits)
    if len(polies) > 0:
        process_polyatomic_ions(polies)
    return polies


def molar_weight_action(args):
    molecule = args.molecule
    print(molecule)

    splits = split(molecule)
    polyatomic_ions = list(filter(filter_polyatomic_ions, splits))
    print(polyatomic_ions)
