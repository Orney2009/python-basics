#!/usr/bin/env python3

def display_all(dictionary):
    try:
        for value in dictionary.values():
            print(f"({type(value).__name__}: {str(value)})")
    except Exception as e:
        print(e)
        exit(84)