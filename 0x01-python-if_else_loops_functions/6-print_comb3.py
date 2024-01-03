#!/usr/bin/python3
for tens in range(10):
    for ones in range(tens + 1, 10):
        print("{}{}".format(tens, ones), end=", " if (tens, ones) != (8, 9) else "\n")
