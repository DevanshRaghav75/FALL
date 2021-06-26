import os
import time
import requests
from colorama import Fore, Style

def subenum():
    print('')
    domain = input(Fore.CYAN + "[SUBENUM] " + Style.RESET_ALL + "[>] Domain: ")

    filename = input(Fore.CYAN + "[SUBENUM] " + Style.RESET_ALL + "[>] Wordlist: ") 
    print(Fore.GREEN + '[INFO] ' + Style.RESET_ALL + "All discovered domains will be auto saved to Discovered_subdomains.txt file.")
    print('')

    with open(filename, "r") as file:
        for subdomain in file.readlines():

            subdomain_url = f"https://{subdomain.strip()}.{domain}"
            
            try:
                response = requests.get(subdomain_url, timeout=3.0)
            
                if response.status_code==200:
                    print(Style.BRIGHT + Fore.GREEN + "[+] " + Fore.WHITE + "Discovered domain: " +(f"{subdomain_url}") + Style.RESET_ALL)
                    os.system('touch Discovered_subdomains.txt')
                    file = open("Discovered_subdomains.txt", 'a')
                    file.write(f"{subdomain_url}")    
                    file.write('\n') 

            except (KeyboardInterrupt):
                yn = input(Style.BRIGHT + Fore.YELLOW + "[>] " + Style.RESET_ALL + "Do you want to exit(y/n): ")
                    
                if yn == 'y':
                    quit()

                elif yn == 'n':
                    print('Restarting...')
                    time.sleep(2)                                                      
            except:
                print(Fore.RED + "[-] " + Style.RESET_ALL + (f"{subdomain_url}"))  
