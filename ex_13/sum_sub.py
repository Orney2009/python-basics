#!/usr/bin/env python3
from functools import reduce
import sys

def add(*args):
    try:
        if len(args[0]) == 0:
            print(0)
        else:
            print(reduce(lambda x, y: int(x) + int(y) if (int(x)%2 != 0) else int(x) - int(y) , args[0]))
    except Exception as e:
        print(e)
        exit(84)

add(sys.argv[1:])