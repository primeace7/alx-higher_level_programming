#!/usr/bin/python3
if __name__ == '__main__':
    names = dir('hidden_4.pyc')
    for name in names:
        if not name.startswith('__'):
            print('{}'.format(name))
