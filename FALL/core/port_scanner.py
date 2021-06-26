import socket
import threading
import concurrent.futures
from colorama import Fore, Style

def port_scanner():
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