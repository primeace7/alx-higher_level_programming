#!/usr/bin/python3
if __name__ == '__main__':
    names = sorted(dir('hidden_d'))
    for name in names:
        if not name.startswith('__'):
            print('{}'.format(name))
