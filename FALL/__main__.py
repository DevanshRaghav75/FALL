#!/usr/bin/python3
# -*- coding: utf-8 -*-

from FALL.core.clear import clear
from FALL.core.dirbrute import dirbrute
from FALL.core.crawler import crawler
from FALL.core.displayoptions import displayoptions
from FALL.core.encoder import encoder
from FALL.core.exit import exit
from FALL.core.LFI import LFI
from FALL.core.openred import openred
from FALL.core.port_scanner import port_scanner
from FALL.core.reversegen import reversegen
from FALL.core.subenum import subenum 
from colorama import Fore, Style



print(Fore.GREEN + Style.BRIGHT + ''' 

              ███████╗  █████╗ ██╗     ██╗     
              ██╔════╝ ██╔══██╗██║     ██║     
              █████╗   ███████║██║     ██║    v1.8
              ██╔══╝   ██╔══██║██║     ██║     
              ██║      ██║  ██║███████╗███████╗
              ╚═╝      ╚═╝  ╚═╝╚══════╝╚══════╝
              ''')
print(Fore.WHITE + Style.BRIGHT + '       :.:.:Coded with' + Fore.RED + " <3 " + Fore.WHITE + 'via: @Hs Devansh Raghav:.:.:' + Style.RESET_ALL)
print('')

def options():
    print('====>  ' + "[1] " + Fore.CYAN + "Crawler" + Style.RESET_ALL )
    print('====>  ' + "[2] " + Fore.CYAN + "LFI testing" + Style.RESET_ALL)
    print('====>  ' + "[3] " + Fore.CYAN + "Encoder" + Style.RESET_ALL)
    print('====>  ' + "[4] " + Fore.CYAN + "Subdomain enumeration" + Style.RESET_ALL)
    print('====>  ' + "[5] " + Fore.CYAN + "Directory brute forcing" + Style.RESET_ALL)
    print('====>  ' + "[6] " + Fore.CYAN + "Reverse shell generator" + Style.RESET_ALL)
    print('====>  ' + "[7] " + Fore.CYAN + "Open redirect testing" + Style.RESET_ALL)
    print('====>  ' + "[8] " + Fore.CYAN + "Multithreaded port scanner" + Style.RESET_ALL)
    print('')
    print('====>  ' + "[C] " + Fore.GREEN + "Clear" + Style.RESET_ALL)
    print('====>  ' + "[X] " + Fore.RED + "Exit" + Style.RESET_ALL)
    print('====>  ' + "[O] " + Fore.YELLOW + "Display Options" + Style.RESET_ALL)
    print('')

options()


def main():

    while True:
        try:
            handler = input("[>]" + " SET: ")  
                           
            if handler == '1':
                crawler()

            elif handler == '2':
                LFI()

            elif handler == '3':
                encoder()
                
            elif handler == '4':
                subenum()

            elif handler == '5':
                dirbrute()

            elif handler == '6':
                reversegen()

            elif handler == '7':
                openred()

            elif handler == '8':
                port_scanner()

            elif handler == 'C':
                clear()

            elif handler == 'X':
                exit()

            elif handler == 'O':
                displayoptions()


        except KeyboardInterrupt:
            print('')
            yn = input(Fore.YELLOW + "[!]" + Style.RESET_ALL + " Do you want to exit FALL (y/n): ")
            print('')

            if yn == 'y':
                quit()

            if yn == 'n':
                print("Restarting...")
                continue


















    



