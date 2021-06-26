import html
import base64
import hashlib
from colorama import Fore, Style

def encoder():
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