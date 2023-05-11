#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv
    length = len(args)
    sum = 0
    if length > 1:
        for i in range(1, length):
            sum += int(args[i])
    print(sum)
