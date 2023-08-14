#!/usr/bin/python3
import calculator_1

def main():
    """The main function."""
    if len(sys.argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])

    if operator == "+":
        result = calculator_1.add(a, b)
    elif operator == "-":
        result = calculator_1.subtract(a, b)
    elif operator == "*":
        result = calculator_1.multiply(a, b)
    elif operator == "/":
        result = calculator_1.divide(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print(f"{a} {operator} {b} = {result}")

if __name__ == "__main__":
    main()
