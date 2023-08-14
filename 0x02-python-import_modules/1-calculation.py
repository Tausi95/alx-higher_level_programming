#!/usr/bin/python3
a = 10
b = 5
calculator = __import__('calculator_1')

add_result = calculator.add(a, b)
sub_result = calculator.sub(a, b)
mul_result = calculator.mul(a, b)
div_result = calculator.div(a, b)

print("{} + {} = {}".format(a, b, add_result))
print("{} - {} = {}".format(a, b, sub_result))
print("{} * {} = {}".format(a, b, mul_result))
print("{} / {} = {}".format(a, b, div_result))
