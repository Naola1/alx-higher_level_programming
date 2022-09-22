#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = int(len(sys.argv))
    if a == 0:
        print('0 arguments.')
    else:
        print('{} arguments:'.format(a - 1))
        for i in range(1, a):
            print('{}: {}'.format(i, sys.argv[i]))
