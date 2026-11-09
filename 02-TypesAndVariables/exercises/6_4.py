# A program that prints detailed information about an employee using string slicing.

employee = "Mr. John May, born on 1998-02-16"

# text[a:b] takes characters from index a up to index b - 1
print(f'Name: {employee[4:8]}')
print(f'Surname: {employee[9:12]}')
print(f'Born: {employee[-10:]}')
print(f'Initials: {employee[4]}{employee[9]}')
