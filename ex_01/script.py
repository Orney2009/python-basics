#!/usr/bin/env python3
import sys

# print("Total arguments:", len(sys.argv))
# print("Script name:", sys.argv[0])
# print("Arguments:", sys.argv[1:])

def asciiCounter(string):
    try:
        count = 0
        if type(string) == str:
            for letter in arg:
                if (48 <= ord(letter) <= 57) or (65 <= ord(letter) <= 90) or (97 <= ord(letter) <= 122) :
                    count +=1
        return count
    except Exception as e:
        print(e)
        exit(84)
total = 0

for arg in sys.argv[1:]:
    total += asciiCounter(arg)

print(total)