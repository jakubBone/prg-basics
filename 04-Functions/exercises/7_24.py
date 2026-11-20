# A program with a function that returns the value of an expression with single-digit numbers, + and -.


def evaluate(expression):
    # the expression starts with a digit, then pairs "operator digit" follow
    result = int(expression[0])
    i = 1
    while i < len(expression):
        operator = expression[i]
        digit = int(expression[i + 1])
        if operator == '+':
            result += digit
        else:
            result -= digit
        i += 2
    return result


if __name__ == "__main__":
    print('f("2+3") returns', evaluate("2+3"))  # 5
    print('f("3+8+1") returns', evaluate("3+8+1"))  # 12
    print('f("2+3-4+5-0") returns', evaluate("2+3-4+5-0"))  # 6
