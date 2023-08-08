#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if('a' <= ord(i) <= 'z'):
            if(97 <= ord(i) <= 122):
                i = chr(ord(i) - 32)
        print("{:s}".format(i), end="")
    print("")
