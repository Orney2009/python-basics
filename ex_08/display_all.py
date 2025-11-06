#!/usr/bin/env python3

def display_all(dictionary):
    try:
        for key, value in dictionary.items():
            print(f"{key}->({type(value).__name__}: {str(value)})")
    except Exception as e:
        print(e)
        exit(84)