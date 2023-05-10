#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if i != j and i < j:
            if i == 8 and j == 9:
                print(f"{i}{j}", end='')
            else:
                print(f"{i}{j}, ", end='')
