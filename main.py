#!/usr/bin/env python

from rich import print
from sys import argv
import argparse
from rich.prompt import Prompt
from rich.console import Console
from rich.prompt import Confirm


__version__ = 'v0.0.1'


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


def interactive():
    """Implementing the Interactive Questioning Mode"""
    print(
        "\n[[bold green]+[/bold green]] Enter the information about the target to make a dictionary")
    print("[[bold yellow]*[/bold yellow]] If you don't know all the info, just hit Enter when asked! ;)\n")

    # we need some information first!

    profile = {}

    console = Console()
    name = str(input("> First Name: ")).lower()
    while len(name) == 0 or name == ' ' or name == '  ' or name == '   ':
        console.log("[*] You must enter a name atleast!", style='bold yellow')
        name = input("> First Name: ").lower()
    profile["name"] = name
    profile["surname"] = str(input("> Surname: ")).lower()
    profile["nick"] = str(input("> Nickname: ")).lower()
    birthdate = str(input("> Birthdate (DDMMYYYY): ")).lower()
    while len(birthdate) != 0 and len(birthdate) != 8:
        console.log("[*] You must enter 8 digits for birthdate!",
                    style='bold yellow')
        birthdate = str(input("> Birthdate (DDMMYYYY): ")).lower()
    profile["birthdate"] = birthdate

    print()

    profile["wife"] = str(input("> Partner's Name: ")).lower()
    profile["wifen"] = str(input("> Nickname: ")).lower()
    wifeb = str(input("> Partner's Birthdate (DDMMYYYY): "))
    while len(wifeb) != 0 and len(wifeb) != 8:
        console.log("[*] You must enter 8 digits for birthday!",
                    style='bold yellow')
        wifeb = str(input("> Partner's Birthdate (DDMMYYYY): "))
    profile["wifeb"] = wifeb

    print()

    profile["kid"] = str(input("> Child's Name: ")).lower()
    profile["kidn"] = str(input("> Child's Nickname: ")).lower()
    kidb = str(input("> Child's Birthday (DDMMYYYY): ")).lower()
    while len(kidb) != 0 and len(kidb) != 8:
        console.log("[*] You must enter 8 digits for birthday!",
                    style='bold yellow')
        kidb = str(input("> Child's Birthday (DDMMYYYY): ")).lower()
    profile["kidb"] = kidb

    print()

    profile["pet"] = str(input("> Pet's Name: ")).lower()
    profile["company"] = str(input("> Company Name: ")).lower()

    print()

    words = ''
    word_perm = Confirm.ask(
        "> Do you want to add some keywords about the target ?", default=False)
    if (word_perm):
        words = input(
            "> Enter words seperated by comma. [i.e. hacker,security,crack]: ").replace(" ", "")
    profile["words"] = words.split(",")

    profile["specialchars"] = Confirm.ask(
        "> Do you want to add special chars at the end of the words?", default=False)
    profile["randnum"] = Confirm.ask(
        "> Do you want to add special chars at the end of the words?", default=False)
    profile["leetmode"] = Confirm.ask(
        "> Leet mode ? (i.e. leet = 1337)", default=False)

    gen_list_from_profile(profile)


def gen_list_from_profile(profile):
    pass


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
