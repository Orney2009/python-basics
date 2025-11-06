#!/usr/bin/env python3

def shows(dictionary):
    try:
        for element in [ f"({key})->({type(value).__name__}: {str(value)})" for (key, value) in dictionary.items() ]:
            print(element)
    except Exception as e:
        print(e)
        exit(84)