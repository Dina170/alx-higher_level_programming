#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    out = 0
    lastvalue = 0
    romans = {'I': 1,
              'V': 5,
              'X': 10,
              'L': 50,
              'C': 100,
              'D': 500,
              'M': 1000}
    for i in reversed(roman_string):
        for k, v in romans.items():
            if k == i:
                if i == len(roman_string) - 1 or v >= lastvalue:
                    out += v
                else:
                    out -= v
                lastvalue = v
    return out
