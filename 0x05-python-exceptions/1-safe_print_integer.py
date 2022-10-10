#!/usr/bin/python3

def safe_print_integer(value):
    try:
        a = int(value)
        print(a)
        return True
    except(ValueError, TypeError):
        return False
