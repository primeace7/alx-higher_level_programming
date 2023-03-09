#!/usr/bin/python3
names = sorted(dir('hidden_d'))
if __name__ == '__main__':
    for name in names:
        if not name.startswith('__'):
            print('{}'.format(name))
