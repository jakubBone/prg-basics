# A program with a function that compares two arrays: they are the same if they have the same length
# and the elements with the same index are equal.


def compare(array1, array2):
    if len(array1) != len(array2):
        return False
    for i in range(len(array1)):
        if array1[i] != array2[i]:
            return False
    return True


def array_to_text(arr):
    text = ''
    for value in arr:
        text = text + str(value) + ' '
    return text


pairs = [
    (["water", "book", "sky"], ["water", "book", "sky"]),
    ([True, False], [True, False, True]),
    ([5, 3, 1], [5, 3, 1]),
    ([3, 2, 1], [3, 2]),
]

for array1, array2 in pairs:
    print('Array1:', array_to_text(array1))
    print('Array2:', array_to_text(array2))
    if compare(array1, array2):
        print('Comparison: arrays are the same')
    else:
        print('Comparison: arrays are different')
    print()
