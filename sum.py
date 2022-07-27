from random import random


def sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


random_numbers = [random() for i in range(10)]
result = sum(*random_numbers)
print(result)