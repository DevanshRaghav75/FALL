<h1 align="center">FALL</h1>
<p align="center"><img src="https://github.com/DevanshRaghav75/FALL/blob/main/FALL%20logo.png"  width="300" height="300" />
<h3 align="center">A tool with multiple features !</h3>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub version](https://badge.fury.io/gh/DevanshRaghav75%2FFALL.svg)](https://github.com/DevanshRaghav75/FALL)
[![GitHub release](https://img.shields.io/github/release/DevanshRaghav75/FALL/FALL.py.svg)](https://GitHub.com/DevanshRaghav75/FALL/releases/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![GitHub commits](https://img.shields.io/github/commits-since/DevanshRaghav75/FALL/1.0.svg)](https://GitHub.com/DevanshRaghav75/FALL/commit/main)
[![Github all releases](https://img.shields.io/github/downloads/DevanshRaghav75/FALL/total.svg)](https://GitHub.com/DevanshRaghav75/FALL/releases/)




## Features🍳
```features
1. Url crawling
2. LFI testing
3. Encoder
4. Subdomains finder
5. Directory brute forcing
6. Reverse shell generator
7. Open Redirection testing
```
## Installation⚙️
```installation
1. sudo git clone https://github.com/DevanshRaghav75/FALL.git
2. sudo chmod +x FALL.py
3. sudo pip install -r requirement.txt
```
## Usage 👨‍💻
```usage
sudo python3 FALL.py
```
## Examples and screenshots 💥

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






