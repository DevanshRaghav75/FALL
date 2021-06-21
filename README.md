<h1 align="center">FALL</h1>
<p align="center"><img src="https://github.com/DevanshRaghav75/FALL/blob/main/FALL%20logo.png"  width="300" height="300" />
<h3 align="center">A tool with multiple features !</h3>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GitHub tag](https://img.shields.io/github/tag/DevanshRaghav75/FALL.svg)](https://GitHub.com/DevanshRaghav75/FALL/tags/)
[![GitHub release](https://img.shields.io/github/release/DevanshRaghav75/FALL.svg)](https://GitHub.com/DevanshRaghav75/FALL/releases/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)


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

<img src="https://github.com/DevanshRaghav75/FALL/blob/main/examples/crawl_urls.png" width="600" height="550" /><br>
<br>
<h3>## LFI testing</h3>
<br>

```crawler
[>] SET: 2
[>] URL: https://www.example.com/?q=FUZZ
[>] Payloads: /path/to/payloads/lfi_payloads.txt
[>] Placeholder: FUZZ
```

<img src="https://github.com/DevanshRaghav75/FALL/blob/main/examples/LFI_testing.png" width="750" height="400" /><br>
<br>
<h3>## Encoder</h3>
<br>

```crawler
[>] SET: 3
[>] Enter encoding: HTML
[>] Enter what you want to encode: <script>alert(1)</script>
```

<br>
<img src="https://github.com/DevanshRaghav75/FALL/blob/main/examples/encoder.png" width="550" height="350" /><br>
<br>
<h3>## Finding subdomains</h3>
<br>

```crawler
[>] SET: 4
[>] Domain: example.com
[>] Wordlist: /path/to/wordlist/wordlist.txt
```

<br>
<img src="https://github.com/DevanshRaghav75/FALL/blob/main/examples/Subdomain_enum.png" width="560" height="400" /><br>
<br>
<h3>## Reverse shell generator</h3>
<br>

```crawler
[>] SET: 5
[>] Shell: BASH
[>] LHOST: 192.168.x.x
[>] LPORT: 8080
```

<br>
<img src="https://github.com/DevanshRaghav75/FALL/blob/main/examples/reverse_shell_generator.png" width="600" height="300" /><br>
<br>
<h3>## Open redirection testing</h3>
<br>

```crawler
[>] SET: 7
[>] URL: http://testphp.vulnweb.com:80/redir.php?r=FUZZ
[>] Payloads: /path/to/payloads/payload.txt
[>] Placeholder: FUZZ
```

<br>
<img src="https://github.com/DevanshRaghav75/FALL/blob/main/examples/OpenRedirection_testing.png" width="700" height="350" />





