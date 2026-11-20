# A program with a function that returns a randomly selected element of an array.

import random


def rand_elem(array):
    # a random valid index: from 0 to len(array) - 1
    index = random.randint(0, len(array) - 1)
    return array[index]


fruits = ["apple", "banana", "cherry", "orange", "plum"]

for i in range(5):
    print(rand_elem(fruits))
