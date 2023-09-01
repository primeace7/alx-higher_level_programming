#!/usr/bin/python3

'''
script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
'''

if __name__ == '__main__':
    import sys
    import requests

    username = sys.argv[1]
    token = 'Bearer {}'.format(sys.argv[2])
    url = "https://api.github.com/{}".format(username)
    payload = {'Authorization': token, 'accept': 'application/vnd.github+json',
               'X-GitHub-Api-Version': '2022-11-28'}

    info = requests.get(url, headers=payload)

    print(info.json().get('id'))
