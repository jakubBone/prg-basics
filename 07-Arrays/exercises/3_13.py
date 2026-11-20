# A program with a function bubblesort() that returns a sorted array. It sorts three arrays.


def bubblesort(array):
    # the list is sorted in place: the original list is changed and the same list is returned
    n = len(array)
    for i in range(n):
        for j in range(n - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
    return array


array1 = [5, 2, 9, 1, 7]
array2 = [10, -3, 8, 0, 15, -20]
array3 = [4, 4, 1, 3]

print('Before:', array1)
print('After: ', bubblesort(array1))
print('Before:', array2)
print('After: ', bubblesort(array2))
print('Before:', array3)
print('After: ', bubblesort(array3))
