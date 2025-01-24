#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: stx@libera.chat
# 2024-03-12
# Updated 2024-11-21 
# Version 2.0: 2025-01-24
import sys
from colorama import Fore
import random
import time

# Dont use these colors.
bad_colors = ['RESET', 'BLACK', 'LIGHTBLACK_EX', 'LIGHTWHITE_EX', 'BLUE', 'RED', 'LIGHTRED_EX']

#Possible colors: 
# BLACK, BLUE, CYAN, GREEN, LIGHTBLACK_EX, LIGHTBLUE_EX, LIGHTCYAN_EX, 'LIGHTGREEN_EX, LIGHTMAGENTA_EX, LIGHTRED_EX, LIGHTWHITE_EX,
# LIGHTYELLOW_EX, MAGENTA, RED, RESET, WHITE, YELLOW

# Patterns to look for; fill in as needed.
My_Patterns = { 
    "K-Line": "LIGHTRED_EX",
    "failed": "LIGHTCYAN_EX",
    }

PATTERN1 = "k-line"
PATTERN2 = "failed"

codes = vars(Fore)
mycolors = [codes[color] for color in codes if color not in bad_colors]

#my_colored_line = ""

def readlog(logfile):
    match_printed = False
    my_colored_line = ""

    #global my_colored_line
    with open(logfile, 'r') as fd:
        fd.seek(0,2)
        while True:
            #for line in fd:
            line = fd.readline()        # One line at a time
            if not line:
                continue
            my_colored_line = random.choice(mycolors) + line

            match_printed = False

            for key in My_Patterns:
                if key.lower() in line.lower():
                    hilight = getattr(Fore, My_Patterns[key].upper(), Fore.RESET)
                    print(f"{hilight}{line}{Fore.RESET}", end='')
                    match_printed = True
                    break

            if not match_printed:
                print(f"{my_colored_line}{Fore.RESET}", end='')

            time.sleep(0.1)


if len(sys.argv) < 2:
    print("Supply a filename to tail.")
else:
    try:
        readlog(sys.argv[1])
    except KeyboardInterrupt:
        # Reset colors.
        print(Fore.RESET)
        print("Shutting down.")
    except FileNotFoundError:
        print("Error: File not found")

