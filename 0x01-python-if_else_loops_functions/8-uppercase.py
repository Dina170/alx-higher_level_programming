#!/usr/bin/python3
def uppercase(str):
    upper_str = ""
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            upper_str += chr(ord(str[i]) - 32)
            continue
        upper_str += str[i]
    print(upper_str)
