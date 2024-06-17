from argparse import ArgumentParser
from molar_weight import molar_weight_action


parser = ArgumentParser()
subparsers = parser.add_subparsers(dest="subcommand")


# Credit to https://mike.depalatis.net/blog/simplifying-argparse.html for the
# helper function and subcommand decorator


def subcommand_arguments(*name_or_flags, **kwargs):
    """
    Helper function to turn a list of arguments and keyword arguments into
    a list and a dict, to use in the subcommand decorator.
    """
    return (list(name_or_flags), kwargs)


def subcommand(args=[], parent=subparsers):
    """
    Decorator to define a subcommand. Add to function (with subcommand's) name, and
    supply (subcommand_arguments() ouptut for) name/flag and attributes.

    Example usage:
    ```
    @subcommand([subcommand_arguments(["molecule", help="Molar weight of supplied molecule"])])
    def molar_weight(args):
        molar_weight_action(args)
    ```

    In the example, the first positional argument will be the molecule. Its value
    can be accessed through the molecule attribute.
    """

    def decorator(func):
        parser = parent.add_parser(func.__name__, description=func.__doc__)
        for arg in args:
            parser.add_argument(*arg[0], **arg[1])
        parser.set_defaults(func=func)

    return decorator


@subcommand(
    [subcommand_arguments("molecule", help="Molar weight of supplied molecule")]
)
def molar_weight(args):
    """
    Calculates the molar weight of the supplied molecule/element.
    Example input: `C2H5OH`, `Fe(OH)2`.  Note that the correctness of the molecule will
    not be checked. Use `check` for this functionality.
    """

    molar_weight_action(args)


if __name__ == "__main__":
    args = parser.parse_args()
    if args.subcommand is None:
        parser.print_help()
    else:
        args.func(args)
