# A program that sums numbers entered by the user until they enter 0, and calculates their arithmetic mean.

total_sum = 0
count = 0  

while True:
    number = int(input("Enter a number (0 to stop): "))

    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    count += 1

print(f"The total sum of the numbers is: {total_sum}")

# the mean is the sum divided by the count; dividing by 0 would raise ZeroDivisionError
if count > 0:
    print(f"The arithmetic mean of the numbers is: {total_sum / count:.2f}")
else:
    print("No numbers were entered, so there is no mean.")
