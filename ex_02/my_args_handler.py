#!/usr/bin/env python3
def my_args_handler(*args):
    try:
        result = ""
        for arg in args:
            result += f"{arg}, "
        return result[:-2]
    except Exception as e:
        print(e)
        exit(84)

