#!/usr/bin/env python

from rich import print
from sys import argv
import argparse
from cupp import __version__
from cupp.functions import interactive


def banner():
    print(" [bold green]_________  ____ _______________________[/bold green]")
    print(" [bold green]\_   ___ \|    |   \______   \______   \ [/bold green]")
    print(" [bold green]/    \  \/|    |   /|     ___/|     ___/[/bold green]")
    print(" [bold green]\     \___|    |  / |    |    |    |    [/bold green]")
    print(" [bold green] \______  /______/  |____|    |____|    [/bold green]")
    print(" [bold green]        \/                              [/bold green]")
    print(" [bold cyan]    Common User Password Profiler[/bold cyan]")
    print("           [bold green]@thehackersbrain[/bold green]")


def version():
    "Display Version"
    print("\n [ [bold white]{0}[/bold white] ] : [bold green]{1}[/bold green]\n \
          \n [[bold green]+[/bold green]] Created by [bold cyan]Gaurav Raj[/bold cyan] - [bold cyan]@thehackersbrain[/bold cyan]\
          \n [[bold green]+[/bold green]] Portfolio: [bold cyan]https://gauravraj.xyz[/bold cyan]\
          \n [[bold green]+[/bold green]] Blog:      [bold cyan]https://blog.gauravraj.xyz[/bold cyan]".format(argv[0], __version__))


def parseArgs():
    """Create and return a argument parse"""
    parser = argparse.ArgumentParser(
        description="Common User Password Profiler")
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Interactive questions for password profiling for a specific target"
    )
    group.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="Show the version information of the Program."
    )
    group.add_argument(
        "-q",
        "--quite",
        action="store_true",
        help="Don't Print the Banner."
    )
    return parser



def main():
    """Command-Line Interface for terminal uses"""

    parser = parseArgs()
    args = parser.parse_args()

    if (not args.quite):
        banner()

    if (args.version):
        version()
    elif (args.interactive):
        interactive()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
