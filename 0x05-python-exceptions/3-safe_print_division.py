#!/usr/bin/python3

ef safe_print_division(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return None
