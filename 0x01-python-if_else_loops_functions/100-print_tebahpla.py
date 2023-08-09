#!/usr/bin/python3
for i in range(25, -1, -1):
    print("{:c}".format(122 - i), end="")
    if i % 2 == 0:
        print("{:c}".format(65 + i), end="")

print("")  # A newline at the end
