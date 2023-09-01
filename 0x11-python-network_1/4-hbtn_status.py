#!/usr/bin/python3

'''
script that fetches data from https://alx-intranet.hbtn.io/status
using reqeusts module
'''

if __name__ == '__main__':
    import requests

    url = 'https://alx-intranet.hbtn.io/status'

    res = requests.get(url)

    print('Body response:')
    print('\t- type:', type(res.text))
    print('\t- content:', res.text)
