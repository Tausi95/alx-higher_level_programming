#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    arg_c = len(sys.argv) - 1
    print(f"{arg_c} argument{'s'if arg_c == 0 || arg_c > 1 else''}", end="")
    print(f"{'.' if arg_c == 0 else ':'}")
    if (arg_c > 0):
        for arg in sys.argv:
            if sys.argv.index(arg) != 0:
               print(f"(sys.argv.index(arg)}: {arg}")
