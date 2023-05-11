#!/usr/bin/python3
import sys
if __name__ == "__main__":
    args = sys.argv
    length = len(args) - 1
    if length > 1:
        for i in range(1, length + 1):
            print("{:d} arguments:".format(length))
            print("{:d}: {:s}".format(i, args[i]))
    elif length == 1:
        print("1 argument.")
        print("1: {:s}".format(args[1]))
    else:
        print("0 arguments.")
