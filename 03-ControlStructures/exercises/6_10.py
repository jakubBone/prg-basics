# A program that calculates a dog's age in dog's years.
# The first two years are worth 10.5 each, every next year is worth 4.

age = int(input("Enter the dog's age in human years: "))

if age <= 2:
    dog_age = age * 10.5
else:
    # the first 2 years: 2 * 10.5 = 21, then 4 for each remaining year
    dog_age = 21 + (age - 2) * 4

# :g prints 73 instead of 73.0
print(f"The dog's age in dog's years is {dog_age:g} years.")
