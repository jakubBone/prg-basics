# A program with a function that sorts a list of numbers using the bubble sort algorithm.


def bubble_sort(arr):
    # the list is sorted in place: the original list is changed and the same list is returned
    n = len(arr)
    # after each pass of the outer loop the largest remaining element is at the end
    for i in range(n):
        for j in range(n - i - 1):
            # compare adjacent elements and swap them if they are in the wrong order
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption)
print(sorted_car_fuel_consumption)

bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
print(bank_transactions)
sorted_bank_transactions = bubble_sort(bank_transactions)
print(sorted_bank_transactions)
