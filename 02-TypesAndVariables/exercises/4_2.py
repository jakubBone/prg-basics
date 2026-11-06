###
# A program that calculates and prints
# the income of a family per person. 
# 
# To print the results in a readable form, uses f-strings.
#

father_income = 5450
mother_income = 4920
family_members = 5
total_income = father_income + mother_income
income_per_person = total_income / family_members

# PEP 8 suggest print up to 79 chars
print(f'Total family income is {total_income:.2f}')
print(f'Income per person is {income_per_person:.2f}')