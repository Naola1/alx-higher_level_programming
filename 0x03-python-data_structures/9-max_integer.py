#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    else:
        for i in my_list:
            for j in range(1, len(my_list)):
                if i < my_list[j]:
                    i = my_list[j]
    return i
