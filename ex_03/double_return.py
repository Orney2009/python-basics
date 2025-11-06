#!/usr/bin/env python3

def double_return(dictionary):
    try:
        keys = list(dictionary.keys())
        values = list(dictionary.values())
        return keys, values
    except Exception as e:
        print(e)
        exit(84)