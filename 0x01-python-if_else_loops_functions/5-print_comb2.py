#!/usr/bin/python3
for i in range(0, 100):
    if (x < 99):
        print("{:d}".format((i // 10), (x % 10)), end=", ")
    else:
        print("{:d}{:d}".format((x // 10), (x % 10)))
