# A module with functions that operate on an array of numbers (MyArrays).
# The file name is in lowercase (my_arrays), because PEP 8 recommends lowercase names for modules.
# The functions max(), min() and sorted() are not used.

def second_largest(arr):
    # the largest element
    largest = arr[0]
    for value in arr:
        if value > largest:
            largest = value
    # the largest element among those that are smaller than the largest one
    second = None
    for value in arr:
        if value < largest and (second is None or value > second):
            second = value
    return second


def min_max(arr):
    smallest = arr[0]
    largest = arr[0]
    for value in arr:
        if value < smallest:
            smallest = value
        if value > largest:
            largest = value
    return [smallest, largest]


def difference(arr):
    smallest_and_largest = min_max(arr)
    return smallest_and_largest[1] - smallest_and_largest[0]


def median(arr):
    # arr[:] is a copy of the list, so the original is not changed
    ordered = arr[:]
    # bubble sort
    n = len(ordered)
    for i in range(n):
        for j in range(n - i - 1):
            if ordered[j] > ordered[j + 1]:
                temp = ordered[j]
                ordered[j] = ordered[j + 1]
                ordered[j + 1] = temp
    middle = n // 2
    if n % 2 == 1:
        return ordered[middle]
    # an even number of elements: the median is the mean of the two middle values
    return (ordered[middle - 1] + ordered[middle]) / 2


def to_text(arr):
    # the elements as a string, separated by the minus sign
    text = ''
    for i in range(len(arr)):
        if i > 0:
            text = text + '-'
        text = text + str(arr[i])
    return text
