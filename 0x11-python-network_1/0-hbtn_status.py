#!/usr/bin/python3

'''
script that fetches data from https://alx-intranet.hbtn.io/status
'''

if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as req:
        print('Body response')
        response = req.read()
        print('\t- type:', type(response))
        print('\t- content:', response)
        print('\t- utf8 content:', response.decode('utf-8'))
