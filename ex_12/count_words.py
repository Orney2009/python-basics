#!/usr/bin/env python3

def my_count_words(param):
    try:
        return {key : param.count(key) for key in param }
    except Exception as e:
        print(e)
        exit(84)