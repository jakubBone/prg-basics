# A program that prints statistics of a test: the number of questions, correct and incorrect answers, the percentage.

test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]

# calculates the number of test questions
question_number = len(test_results)

# calculates the number of correct answers (the value True means a correct answer)
correct_answers = 0
for answer in test_results:
    if answer:
        correct_answers += 1

# calculates the number of incorrect answers
incorrect_answers = question_number - correct_answers

# calculates the percentage of correct answers
percentage = correct_answers / question_number * 100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print(f'Percentage of correct answers: {percentage:.1f}%')
