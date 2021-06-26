import requests
import os
from colorama import Fore, Style

def dirbrute():
    print('')
    print(Fore.GREEN + "[INFO]" + Style.RESET_ALL + " Make sure you do not add Backslash(/) after the URL, Your URL should be : http://example.com or https://example.com")
    print('')
    dirb = input(Fore.CYAN + "[DIR-BRUTE]" + Style.RESET_ALL + "[>] URL: ")
    dirb2 = input(Fore.CYAN + "[DIR-BRUTE]" + Style.RESET_ALL + "[>] Wordlist: ")
    print('')

    with open (str(dirb2)) as wordlist: 
        read = wordlist.readlines() 
            
        
    for line in read:
        
        path_of_url = str(dirb + "/" + line) 
        r = requests.get(path_of_url, timeout=2.0) 
        response = r.status_code
        
        if response == 200:

            print(Style.BRIGHT + Fore.GREEN + "[200] " + Fore.WHITE + "Valid Path Found: " + Style.BRIGHT + path_of_url + Style.RESET_ALL)
            os.system('touch DIR-BRUTE_result.txt')
            file = open('DIR-BRUTE_result.txt', "a")
            file.write((str(response)) + ": " + path_of_url)

        elif response == 404: 
            print(Style.BRIGHT + Fore.RED + "[404] " + Style.RESET_ALL + "Path Not Found: " + path_of_url)
                
        elif response == 302: 
            print(Style.BRIGHT + Fore.GREEN + "[302] " + "Potential EAR vulnerability found: " + path_of_url)
        

