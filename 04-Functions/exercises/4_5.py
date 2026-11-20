# A program that calculates the final grade for a test based on the number of points obtained.


def pts_to_grade(points):
    # the conditions are checked from the top, so the highest grade has to be checked first
    grade = ''
    if points >= 18:
        grade = 'Excellent'
    elif points >= 14:
        grade = 'Good'
    elif points >= 10:
        grade = 'Satisfactory'
    else:
        grade = 'Fail'
    return grade


test_result = 15
final_grade = pts_to_grade(test_result)
print(f'You scored {test_result} points on the test. Your final grade is {final_grade}')
