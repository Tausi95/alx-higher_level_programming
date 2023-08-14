#!/usr/bin/python3
import dis
import types

def print_hidden_names():
    with open("hidden_4.pyc", "rb") as file:
        code = file.read()

    code = code[8:]  # Remove the magic number and timestamp

    module = types.ModuleType("hidden_4")
    exec(code, module.__dict__)

    for name in dir(module):
        if not name.startswith("__"):
            print(name)

if __name__ == "__main__":
    print_hidden_names()
