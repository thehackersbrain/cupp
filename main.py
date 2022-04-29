#!/usr/bin/env python

from rich import print
from sys import argv
import argparse
from rich.prompt import Prompt
from rich.console import Console
from rich.prompt import Confirm
import os
import configparser
import functools
from sys import exit
from time import sleep


__version__ = 'v0.0.1'

# CONFIG = {}


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


class CONFIG_DATA:
    years = []
    for i in range(1990, 2023):
        years.append(i)
    chars = ['!','@','#','$','%%','&','*']
    leet = {"a": "4", "i": "1", "e": "3", "t": "7", "o": "0", "s": "5", "g": "9", "z": "2"}
    threshold = 200
    wcfrom = 5
    wcto = 12


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
        "> Do you want to add random numbers at the end of the words?", default=False)
    profile["leetmode"] = Confirm.ask(
        "> Leet mode ? (i.e. leet = 1337)", default=False)

    gen_list_from_profile(profile)


def make_leet(x):
    """convert string to leet"""
    for letter, leetletter in CONFIG_DATA.leet:
        x = x.replace(letter, leetletter)
    return x


def concats(seq, start, stop):
    """for concatenations..."""
    for i in seq:
        for j in range(start, stop):
            yield i + str(j)


def komb(seq, start, special=''):
    for i in seq:
        for j in start:
            yield str(i) + str(special) + str(j)


def gen_list_from_profile(profile):
    """Generates a wordlist from a given profile"""

    # chars = CONFIG["global"]["chars"]
    # years = CONFIG["global"]["years"]
    # numfrom = CONFIG["global"]["numfrom"]
    # numto = CONFIG["global"]["numto"]
    chars = CONFIG_DATA.chars
    years = CONFIG_DATA.years
    numfrom = 0
    numto = 100

    profile["spechars"] = []

    if (profile["specialchars"]):
        for i in chars:
            profile["spechars"].append(i)
            for j in chars:
                profile["spechars"].append(i + j)
                for k in chars:
                    profile["spechars"].append(i + j + k)

    print("\r\n[[bold green]+[/bold green]] Now making a dictionary...")

    # Now we must do some string modifications...

    # Birthdays first
    birthdate_yy = profile["birthdate"][-2:]
    birthdate_yyy = profile["birthdate"][-3:]
    birthdate_yyyy = profile["birthdate"][-4:]
    birthdate_xd = profile["birthdate"][1:2]
    birthdate_xm = profile["birthdate"][3:4]
    birthdate_dd = profile["birthdate"][:2]
    birthdate_mm = profile["birthdate"][2:4]

    wifeb_yy = profile["wifeb"][-2:]
    wifeb_yyy = profile["wifeb"][-3:]
    wifeb_yyyy = profile["wifeb"][-4:]
    wifeb_xd = profile["wifeb"][1:2]
    wifeb_xm = profile["wifeb"][3:4]
    wifeb_dd = profile["wifeb"][:2]
    wifeb_mm = profile["wifeb"][2:4]

    kidb_yy = profile["kidb"][-2:]
    kidb_yyy = profile["kidb"][-3:]
    kidb_yyyy = profile["kidb"][-4:]
    kidb_xd = profile["kidb"][1:2]
    kidb_xm = profile["kidb"][3:4]
    kidb_dd = profile["kidb"][:2]
    kidb_mm = profile["kidb"][2:4]

    # Convert first letters to uppercase...
    nameup = profile["name"].capitalize()
    surnameup = profile["surname"].capitalize()
    nickup = profile["nick"].capitalize()
    wifeup = profile["wife"].capitalize()
    wifenup = profile["wifen"].capitalize()
    kidup = profile["kid"].capitalize()
    kidnup = profile["kidn"].capitalize()
    petup = profile["pet"].capitalize()
    companyup = profile["company"].capitalize()

    wordsup = []
    wordsup = list(map(str.capitalize, profile["words"]))
    word = profile["words"] + wordsup

    # reverse a name
    rev_name = profile["name"][::-1]
    rev_nameup = nameup[::-1]
    rev_nick = profile["nick"][::-1]
    rev_nickup = nickup[::-1]
    rev_wife = profile["wife"][::-1]
    rev_wifeup = wifeup[::-1]
    rev_kid = profile["kid"][::-1]
    rev_kidup = kidup[::-1]

    reverse = [
        rev_name,
        rev_nameup,
        rev_nick,
        rev_nickup,
        rev_wife,
        rev_wifeup,
        rev_kid,
        rev_kidup
    ]

    rev_n = [
        rev_name,
        rev_nameup,
        rev_nick,
        rev_nickup
    ]

    rev_w = [
        rev_wife,
        rev_wifeup
    ]

    rev_k = [
        rev_kid,
        rev_kidup
    ]

    # Let's do some serious work! This will be a mess of code
    # But... who cares? ;)

    # Birthday combinations
    bds = [
        birthdate_yy,
        birthdate_yyy,
        birthdate_yyyy,
        birthdate_xd,
        birthdate_xm,
        birthdate_dd,
        birthdate_mm,
    ]

    bd_wordlist = []

    for i in bds:
        bd_wordlist.append(i)
        for j in bds:
            if (bds.index(i) != bds.index(j)):
                bd_wordlist.append(i + j)
                for k in bds:
                    if (bds.index(i) != bds.index(j)
                        and bds.index(j) != bds.index(k)
                        and bds.index(i) != bds.index(k)
                        ):
                        bd_wordlist.append(i + j + k)

    # For wife's Birthdays
    wbds = [
        wifeb_yy,
        wifeb_yyy,
        wifeb_yyyy,
        wifeb_xd,
        wifeb_xm,
        wifeb_dd,
        wifeb_mm
    ]

    wbd_wordlist = []

    for i in wbds:
        wbd_wordlist.append(i)
        for j in wbds:
            if (wbds.index(i) != wbds.index(j)):
                wbd_wordlist.append(i + j)
                for k in wbds:
                    if (wbds.index(i) != wbds.index(j)
                        and wbds.index(j) != wbds.index(k)
                        and wbds.index(i) != wbds.index(k)
                        ):
                        wbd_wordlist.append(i + j + k)

    # For wife's Birthdays
    kbds = [
        kidb_yy,
        kidb_yyy,
        kidb_yyyy,
        kidb_xd,
        kidb_xm,
        kidb_dd,
        kidb_mm
    ]

    kbd_wordlist = []

    for i in kbds:
        kbd_wordlist.append(i)
        for j in kbds:
            if (kbds.index(i) != kbds.index(j)):
                kbd_wordlist.append(i + j)
                for k in kbds:
                    if (kbds.index(i) != kbds.index(j)
                        and kbds.index(j) != kbds.index(k)
                        and kbds.index(i) != kbds.index(k)
                        ):
                        kbd_wordlist.append(i + j + k)

    # For string combinations...
    kombinaac = [
        profile["pet"],
        petup,
        profile["company"],
        companyup
    ]

    kombina = [
        profile["name"],
        profile["surname"],
        profile["nick"],
        nameup,
        surnameup,
        nickup,
    ]

    kombinaw = [
        profile["wife"],
        profile["wifen"],
        wifeup,
        wifenup,
        profile["surname"],
        surnameup,
    ]

    kombinak = [
        profile["kid"],
        profile["kidn"],
        kidup,
        kidnup,
        profile["surname"],
        surnameup,
    ]

    kombinaa = []
    for i in kombina:
        kombinaa.append(i)
        for j in kombina:
            if (kombina.index(i) != kombina.index(j)
                    and kombina.index(i.capitalize()) !=
                    kombina.index(j.capitalize())
                ):
                kombinaa.append(i + j)

    kombinaaw = []
    for i in kombinaw:
        kombinaaw.append(i)
        for j in kombinaw:
            if (kombinaw.index(i) != kombinaw.index(j)
                    and kombinaw.index(i.capitalize()) !=
                    kombinaw.index(j.capitalize())
                ):
                kombinaaw.append(i + j)

    kombinaak = []
    for i in kombinak:
        kombinaak.append(i)
        for j in kombinak:
            if (kombinak.index(i) != kombinak.index(j)
                    and kombinak.index(i.capitalize()) !=
                    kombinak.index(j.capitalize())
                ):
                kombinaak.append(i + j)

    kombi = {}
    kombi[1] = list(komb(kombinaa, bd_wordlist))
    kombi[1] += list(komb(kombinaa, bd_wordlist, "_"))
    kombi[2] = list(komb(kombinaaw, wbd_wordlist))
    kombi[2] += list(komb(kombinaaw, wbd_wordlist, "_"))
    kombi[3] = list(komb(kombinaak, kbd_wordlist))
    kombi[3] += list(komb(kombinaak, kbd_wordlist, "_"))
    kombi[4] = list(komb(kombinaa, years))
    kombi[4] += list(komb(kombinaa, years, "_"))
    kombi[5] = list(komb(kombinaac, years))
    kombi[5] += list(komb(kombinaac, years, "_"))
    kombi[6] = list(komb(kombinaaw, years))
    kombi[6] += list(komb(kombinaaw, years, "_"))
    kombi[7] = list(komb(kombinaak, years))
    kombi[7] += list(komb(kombinaak, years, "_"))
    kombi[8] = list(komb(word, bd_wordlist))
    kombi[8] += list(komb(word, bd_wordlist, "_"))
    kombi[9] = list(komb(word, wbd_wordlist))
    kombi[9] += list(komb(word, wbd_wordlist, "_"))
    kombi[10] = list(komb(word, kbd_wordlist))
    kombi[10] += list(komb(word, kbd_wordlist, "_"))
    kombi[11] = list(komb(word, kbd_wordlist))
    kombi[11] += list(komb(word, kbd_wordlist, "_"))
    kombi[12] = [""]
    kombi[13] = [""]
    kombi[14] = [""]
    kombi[15] = [""]
    kombi[16] = [""]
    kombi[21] = [""]

    if (profile["randnum"]):
        kombi[12] = list(concats(word, numfrom, numto))
        kombi[13] = list(concats(kombinaa, numfrom, numto))
        kombi[14] = list(concats(kombinaac, numfrom, numto))
        kombi[15] = list(concats(kombinaaw, numfrom, numto))
        kombi[16] = list(concats(kombinaak, numfrom, numto))
        kombi[21] = list(concats(reverse, numfrom, numto))

    kombi[17] = list(komb(reverse, years))
    kombi[17] += list(komb(reverse, years, "_"))
    kombi[18] = list(komb(rev_w, wbd_wordlist))
    kombi[18] += list(komb(rev_w, wbd_wordlist, "_"))
    kombi[19] = list(komb(rev_k, kbd_wordlist))
    kombi[19] += list(komb(rev_k, kbd_wordlist, "_"))
    kombi[20] = list(komb(rev_n, bd_wordlist))
    kombi[20] += list(komb(rev_n, bd_wordlist, "_"))
    komb001 = [""]
    komb002 = [""]
    komb003 = [""]
    komb004 = [""]
    komb005 = [""]
    komb006 = [""]

    if (len(profile["spechars"]) > 0):
        komb001 = list(komb(kombinaa, profile["spechars"]))
        komb002 = list(komb(kombinaac, profile["spechars"]))
        komb003 = list(komb(kombinaaw, profile["spechars"]))
        komb004 = list(komb(kombinaak, profile["spechars"]))
        komb005 = list(komb(word, profile["spechars"]))
        komb006 = list(komb(reverse, profile["spechars"]))

    print("[[bold green]+[/bold green]] Sorting list and removing duplicates...")

    komb_unique = {}
    for i in range(1, 22):
        komb_unique[i] = list(dict.fromkeys(kombi[i]).keys())

    komb_unique01 = list(dict.fromkeys(kombinaa).keys())
    komb_unique02 = list(dict.fromkeys(kombinaac).keys())
    komb_unique03 = list(dict.fromkeys(kombinaaw).keys())
    komb_unique04 = list(dict.fromkeys(kombinaak).keys())
    komb_unique05 = list(dict.fromkeys(word).keys())
    komb_unique06 = list(dict.fromkeys(komb001).keys())
    komb_unique07 = list(dict.fromkeys(komb002).keys())
    komb_unique08 = list(dict.fromkeys(komb003).keys())
    komb_unique09 = list(dict.fromkeys(komb004).keys())
    komb_unique010 = list(dict.fromkeys(komb005).keys())
    komb_unique011 = list(dict.fromkeys(komb006).keys())

    uniqlist = (
        bd_wordlist
        + kbd_wordlist
        + reverse
        + komb_unique01
        + komb_unique02
        + komb_unique03
        + komb_unique04
        + komb_unique05
    )

    for i in range(1, 12):
        uniqlist += komb_unique[i]

    uniqlist += (
        komb_unique06,
        komb_unique07,
        komb_unique08,
        komb_unique09,
        komb_unique010,
        komb_unique011
    )

    print(type(uniqlist))
    unique_lista = list(dict.fromkeys(uniqlist).keys())
    unique_leet = []
    if (profile["leetmode"]):
        for (x) in (unique_lista):
            x = make_leet(x)
            unique_leet.append(x)

    unique_list = unique_lista + unique_leet

    unique_list_finished = []
    unique_list_finished = [
        x
        for x in unique_list
        if len(x) < CONFIG_DATA.wcto and len(x) > CONFIG_DATA.wcfrom
    ]

    print_to_file(profile["name"] + ".txt", unique_list_finished)


def print_to_file(filename, unique_list_finished):
    with open(filename, "w") as fh:
        unique_list_finished.sort()
        fh.write(os.linesep.join(unique_list_finished))

    with open(filename, "r") as fh:
        lines = 0
        for i in fh:
            lines =+ 1
    Console.log("Wordlist ({}) Created and Saved...".format(filename), style="bold green")
    print("[[bold green]+[/bold green]] Wordlist {0} saved with {1} words.".format(filename, str(lines)))

    inspect = Prompt.ask("> Hyperspeed Print?")
    if (inspect):
        try:
            with open(filename, "r+") as wlist:
                data = wlist.readlists()
                for i in data:
                    print("[bold yellow][{0}][/bold yellow]".format(i))
                    sleep(0000.1)
                    os.system("clear")
        except Exception as e:
            Console.log("{}".format(e), style="bold red")


def main():
    """Command-Line Interface for terminal uses"""

    # read_config(os.path.join(os.path.dirname(os.path.realpath(__file__)), "cupp.cfg"))

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
