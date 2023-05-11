#!/usr/bin/python3

import hiddin_4
if __name__ == "__main__":
    names = dir(hiddin_4)
    for i in names:
        if i[:2] != "__":
            print(i)
