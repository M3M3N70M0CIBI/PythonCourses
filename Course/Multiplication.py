# This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.

x = int(input('Number goes here: '))

mult = lambda x: x * 8 if x % 2 == 0 else x * 9

print(mult(x))