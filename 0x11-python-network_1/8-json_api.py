#!/usr/bin/python3
'''
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
'''

if __name__ == '__main__':
    import sys
    import requests

    url = 'http://0.0.0.0:5000/search_user'

    if len(sys.argv) == 1:
        letter = ''
    else:
        letter = sys.argv[1]

    payload = {'q': letter}

    res = requests.post(url, data=payload)

    try:
        res_json = res.json()

        if len(res_json) == 0:
            print('No result')
        else:
            print('[' + str(res_json.get('id')) + ']',
                  str(res_json.get('name')))

    except requests.exceptions.JSONDecodeError as e:
        print('Not a valid JSON')
