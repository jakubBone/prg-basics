# A program that prints the name of a university with an extra space between the characters.

university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded = university_expanded + char + ' '

print(university)  
print(university_expanded)  
