# A program with a function that returns the result of an arithmetic operation (+, -, *, %, **).


def calculate(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '%':
        return number1 % number2
    elif operator == '**':
        return number1 ** number2
    else:
        # None means "no value"
        return None


if __name__ == "__main__":
    print('f(2,3,"+") returns', calculate(2, 3, '+'))  # 5
    print('f(2,3,"%") returns', calculate(2, 3, '%'))  # 2
    print('f(2,3,"**") returns', calculate(2, 3, '**'))  # 8
    print('f(2,3,"*") returns', calculate(2, 3, '*'))  # 6
    print('f(2,3,"-") returns', calculate(2, 3, '-'))  # -1
