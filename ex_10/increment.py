#!/usr/bin/env python3

def increment(params):
    try:
        return [element + 1 if isinstance(element, int) else element for element in params]
    except Exception as e:
        print(e)
        exit(84)