#!/usr/bin/python3
def uppercase(str):
	for char in s:
		if ord('a') <= ord(char) <= ord('z'):
			upper_char = chr(ord(char) - ord('a') + ord('A'))
			print(upper_char, end="")
		else:
			print(char, end="")
	print()
