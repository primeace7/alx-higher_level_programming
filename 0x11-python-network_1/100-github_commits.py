#!/usr/bin/python3

'''
list 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
'''

if __name__ == '__main__':
    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]

    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)

    res = requests.get(url)

    dates = []
    commits = {}

    res_json = res.json()

    for result in res_json:
        sha = result.get('sha')
        author = result.get('commit').get('author').get('name')
        date = result.get('commit').get('author').get('date')

        dates.append(date)
        commits[date] = sha + ': ' + author

    dates = sorted(dates)

    for i in range(10):
        print(commits[dates[i]])
