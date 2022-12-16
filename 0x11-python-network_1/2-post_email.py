#!/usr/bin/python3
"""ython script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    values = {"email": sys.argv[2]}
    q = urllib.parse.urlencode(values)
    url = f"{sys.argv[1]}?{q}"
    with urllib.request.urlopen(url) as response:
        print(response.read().decode("utf-8"))
