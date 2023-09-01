#!/usr/bin/python3

'''
script that takes in a URL, sends a request to the URL and displays the
value of the variable X-Request-Id in the response header, using
requests module
'''

if __name__ == '__main__':
    import sys
    import requests

    url = sys.argv[1]

    res = requests.get(url)

    print(res.headers['X-Request-Id'])
