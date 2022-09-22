#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    a = int(len(sys.argv))
    print(f'{a - 1} arguments:')
    for i in range(1, a):
        print(f'{i}: {sys.argv[i]}')
