import sys
import time
import requests
from colorama import Fore, Style

def openred():
    print('')
    openr = input(Fore.CYAN + "[OPEN_REDIRECT] " + Style.RESET_ALL + "[>] URL: ")
    openr2 = input(Fore.CYAN + "[OPEN_REDIRECT] " + Style.RESET_ALL + "[>] Payloads: ")
    openr3 = input(Fore.CYAN + "[OPEN_REDIRECT] " + Style.RESET_ALL + "[>] Placeholder: ")
    print('')

    with open(openr2, "r") as file:
        for open_pays in file.readlines():

            replace_holder = openr.replace(openr3, open_pays.strip())

            send = requests.get(replace_holder, timeout=3.0)

            try:         
                if send.history:
                    print(Fore.GREEN + "[INFO] " + Style.RESET_ALL + "Note if the tool will found a redirection it will automatically close the scanning.")
                    print('')
                    print(Style.BRIGHT + Fore.GREEN + "[+] " + Fore.WHITE + "Redirection found: " + replace_holder + Style.RESET_ALL)
                    print('')
                    break
                else:
                    print(Fore.RED + "[-] " + Style.RESET_ALL + replace_holder)
                    
            except KeyboardInterrupt:
                yn = input(Style.BRIGHT + Fore.YELLOW + "[>] " + Style.RESET_ALL + "Do you want to exit(y/n): ")
                    
                if yn == 'y':
                    sys.exit()

                elif yn == 'n':
                    print('Restarting...')
                    time.sleep(2) 
