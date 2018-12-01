Tor Requests
===================
A lib to mimic requests usage and yet try to hide itself from servers. This package was created for educational purposes only, use at your own responsibility.

## Installation
>The commands below may need to be prefixed with `sudo` depending upon your system

```bash
apt-get update
apt-get install tor
pip3 install -r requirements.txt
```

## Usage

Start tor service
```bash
service tor start
```

Python usage is meant to be just like the lib requets itself.

Example:
```bash
import requests
import tor_requests

url = 'https://url-to-fetch.com/'

# Regular requests lib
session = requests.session()
request = session.get(url)
response = request.text

# Tor requests lib
session = tor_requests.session()
request = session.get(url)
request = session.get(url)
response = request.text
```

If you want to check tor's install you can do

```bash
service tor status
```
or to check running port

```bash
apt-get install nmap
nmap -Pn localhost
```


nano /etc/tor/torrc

uncomment these lines
#ControlPort 9051
## If you enable the controlport, be sure to enable one of these
## authentication methods, to prevent attackers from accessing it.
#HashedControlPassword 16:872860B76453A77D60CA2BB8C1A7042072093276A3D701AD684053EC4C

to generate a password
tor --hash-password "vanzan"