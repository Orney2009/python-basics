#!/usr/bin/env python3

def my_show_platypus(times):
    try:
        for time in range (times):
            print("Platypus")
    except Exception as e:
        print(e)
        exit(84)