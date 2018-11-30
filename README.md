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
