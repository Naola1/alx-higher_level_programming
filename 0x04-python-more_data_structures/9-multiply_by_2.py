#!/usr/bin/python3

def multiply_by_2(a_dictionary):
       for keys in sorted(a_dictionary.keys()):
        print('{}: {}'. format(keys, a_dictionary[keys]*2))
