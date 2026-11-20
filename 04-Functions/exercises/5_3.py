# A program that reads and prints employee data. The user decides whether the salary is printed.

import keyboard  # our own module keyboard.py (the same folder as this program)

# Reads employee's data from keyboard
first_name = keyboard.input_string('Enter name: ')
last_name = keyboard.input_string('Enter last name: ')
age = keyboard.input_integer('Enter age: ')
salary = keyboard.input_real('Enter salary: ')
is_salary_hidden = keyboard.input_boolean('Hide salary? (y/n) ')

# Prints employee's record
print('DATA RECORD')
print('===========')
print('Name:', first_name)
print('Last name:', last_name)
print('Age:', age)
if not is_salary_hidden:
    print('Salary:', salary)
