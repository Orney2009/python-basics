#!/usr/bin/env python3

def show_methods(param):
    try:
        methods_list = [ method  for method in dir(param)  ]
        print(methods_list )
    except Exception as e:
        print(e)
        exit(84)
