from argparse import ArgumentParser

main_parser = ArgumentParser()
subparsers = main_parser.add_subparsers(dest="subcommand")


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
    ```python
    @subcommand([subcommand_arguments(["molecule", help="Molecule to calculate molar weight for"])])
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
