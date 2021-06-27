<h1 align="center">FALL</h1>
<p align="center"><img src="https://github.com/DevanshRaghav75/FALL/blob/main/FALL%20logo.png"  width="300" height="300" />
<h3 align="center">A automated penetration testing tool</h3>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub release](https://img.shields.io/github/release/DevanshRaghav75/FALL.svg)](https://GitHub.com/DevanshRaghav75/FALL/releases/tag)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![GitHub commits](https://img.shields.io/github/commits-since/DevanshRaghav75/FALL/1.0-beta.svg)](https://GitHub.com/DevanshRaghav75/FALL/commit/main)
[![GitHub issues-closed](https://img.shields.io/github/issues-closed/DevanshRaghav75/FALL.svg)](https://GitHub.com/DevanshRaghav75/FALL/issues?q=is%3Aissue+is%3Aclosed)
[![GitHub license](https://img.shields.io/github/license/DevanshRaghav75/FALL.svg)](https://github.com/DevanshRaghav75/FALL/blob/master/LICENSE.md)
[![PyPI version shields.io](https://img.shields.io/badge/pypi-v1.5-green)](https://img.shields.io/badge/pypi-v1.5-green)



## What is FALL?

FALL is a automated penetration testing tool that makes your work easy by automating eight types of jobs like - Subdomain enumeration, LFI testing, Crawling, Port scanning and more.

## Why FALL?

1. ```FALL``` supports many options that will help you in penetration testing, In short - It is a ALL IN ONE tool.
2. Multithreaded - Multithreaded ```crawler``` and ```port scanner``` will make your work more fast.
3. ```FALL``` is user friendly and easy to use, You can use ```FALL``` by just setting the options number.
4. It auto saves the outputs in a file.

## PyPi link

```PyPi FALL``` https://pypi.org/project/FALL/

## Features🍳

```features
1. Crawling
2. LFI testing
3. Encoder
4. Subdomains finder
5. Directory brute forcing
6. Reverse shell generator
7. Open Redirection testing
8. Multithreaded port scanner
```
## Installation⚙️

You can also install ```FALL``` using pip
```insall by pip
pip install FALL
```
Or you can install ```FALL``` manually

```installation
1. sudo git clone https://github.com/DevanshRaghav75/FALL.git
2. sudo chmod +x setup.py
3. sudo pip install -r requirements.txt
4. python3 setup.py install
4. Done! , Just type FALL to run FALL tool  
```
## Usage 👨‍💻

```usage
Just type FALL after running the setup.py
```

## Warning⚠️


Up to ```FALL v1.4``` does not work without super user (root user) so make sure you run ```FALL``` as a super user.


## Examples 💥

<h3>## Crawling urls</h1>

```crawler
[>] SET: 1
[>] URL: https://www.example.com
```


<h3>## LFI testing</h3>

```crawler
[>] SET: 2
[>] URL: https://www.example.com/?q=FUZZ
[>] Payloads: /path/to/payloads/lfi_payloads.txt
[>] Placeholder: FUZZ
```

<h3>## Encoder</h3>

```crawler
[>] SET: 3
[>] Enter encoding: HTML
[>] Enter what you want to encode: <script>alert(1)</script>
```

<h3>## Finding subdomains</h3>

```crawler
[>] SET: 4
[>] Domain: example.com
[>] Wordlist: /path/to/wordlist/wordlist.txt
```


<h3>## Reverse shell generator</h3>

```crawler
[>] SET: 5
[>] Shell: BASH
[>] LHOST: 192.168.x.x
[>] LPORT: 8080
```


<h3>## Open redirection testing</h3>

```crawler
[>] SET: 7
[>] URL: http://testphp.vulnweb.com:80/redir.php?r=FUZZ
[>] Payloads: /path/to/payloads/payload.txt
[>] Placeholder: FUZZ
```

<h3>## Multi threaded port scanner</h3>

```port scanner
[>] Target: 192.168.x.x
[>] Scan up to port (ex would be 1000): 65535
```
