#!/usr/bin/python3

'''
script that fetches data from https://alx-intranet.hbtn.io/status
'''

if __name__ == '__main__':
    import urllib.request

    url = 'https://alx-intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as req:
        print('Body response:')
        for line in req.read():
            print('\t-', line)
