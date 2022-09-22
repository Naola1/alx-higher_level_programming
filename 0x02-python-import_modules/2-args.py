#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = int(len(sys.argv))
    if a == 0:
        print('0 arguments.')
    else:
        print(f'{a - 1} arguments:')
        for i in range(1, a):
            print(f'{i}: {sys.argv[i]}')
