#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    nl = my_list.copy()
    if idx < 0 or idx >= len(my_list):
        return nl
    nl[idx] = element
    return nl
