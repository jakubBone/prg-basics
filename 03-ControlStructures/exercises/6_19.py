# A program that prints a survey of three yes-no questions and then shows the survey results.
# The answers are saved in logical (bool) variables.

print('SURVEY')
# answer == 'y' is True only for the answer y, so the variable is a bool
computer_science = input('Are you interested in computer science? (y/n): ') == 'y'
games = input('Do you like playing computer games? (y/n): ') == 'y'
instagram = input('Do you have an Instagram account? (y/n): ') == 'y'

# 'Yes' if the variable is True, otherwise 'No'
print()
print('SURVEY RESULTS')
print(f"Interested in computer science: {'Yes' if computer_science else 'No'}")
print(f"Playing computer games: {'Yes' if games else 'No'}")
print(f"Has an Instagram account: {'Yes' if instagram else 'No'}")
