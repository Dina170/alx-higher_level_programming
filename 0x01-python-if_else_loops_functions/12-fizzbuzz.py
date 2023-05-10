#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        str1 = ""
        if i % 3 == 0:
            str1 += "fizz"
        if i % 5 == 0:
            str1 += "buzz"
        if str1 == "":
            str1 += str(i)
        print(str1, end=" ")
