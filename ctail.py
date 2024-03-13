#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: stx@libera.chat
# 2024-03-12

import sys
from colorama import Fore
import random
import time

# Dont use these colors.
bad_colors = ['RESET', 'BLACK', 'LIGHTBLACK_EX', 'LIGHTWHITE_EX', 'BLUE', 'RED', 'LIGHTRED_EX']

codes = vars(Fore)
mycolors = [codes[color] for color in codes if color not in bad_colors]

def readlog(logfile):
    with open(logfile, 'r') as fd:
        fd.seek(0,2)
        while True:
            for line in fd:
                my_colored_line = random.choice(mycolors) + line

                # We want this in light red.
                if "PATTERN1" in line:
                    print(Fore.LIGHTRED_EX + line + Fore.RESET, end='')
                    continue
                # We want this in red.
                elif "PATTERN2" in line:
                    print(Fore.RED + line + Fore.RESET, end='')  
                    continue
                # Everything else in a random color.
                else:
                    print(my_colored_line, end='')
                    continue

            # Avoid high CPU usage
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

