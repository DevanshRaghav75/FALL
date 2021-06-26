import os
import sys
import os.path
import requests
from colorama import Fore, Style

def LFI():
    print('')
    U = input(Fore.CYAN + "[LFI]" + Style.RESET_ALL + "[>] " + 'URL: ')
    P = input(Fore.CYAN + "[LFI]" + Style.RESET_ALL + "[>] " + 'Payloads: ')
    PH = input(Fore.CYAN + "[LFI]" + Style.RESET_ALL + "[>] " + 'Placeholder: ')
    print('')

    with open (str(P)) as wordlist:
        read = wordlist.readlines()

    for each_line in read:
        path_of_url = U.replace(PH , each_line)
        request_send = requests.get(path_of_url) 
        response = request_send.status_code

        if response == 200:
            print(Fore.GREEN + "[HIGH] " + Style.RESET_ALL + "Potential LFI vulnerability found: " + path_of_url)
            os.system('touch LFI_vulnerable_urls.txt')
            file = open('LFI_vulnerable_urls.txt', 'a')
            file.write(path_of_url)
            file.write('\n')

        elif response == 403:
            print(Fore.YELLOW + "[403] " + Style.RESET_ALL + "Try some 403 Forbidden bypass payloads: " + path_of_url)

        elif response == 404:
            print(Fore.RED + "[404] " + Style.RESET_ALL + "Not found: " + path_of_url)