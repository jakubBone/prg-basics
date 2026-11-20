# A program with a function that returns the sum of the repeated digits in a number.


def sum_repeated_digits(number):
    text = str(abs(number))
    total = 0
    for char in text:
        # count() returns how many times the digit appears; a digit that appears more than once is repeated
        if text.count(char) > 1:
            total += int(char)
    return total


if __name__ == "__main__":
    print('f(1027) returns', sum_repeated_digits(1027))  # 0
    print('f(230335) returns', sum_repeated_digits(230335))  # 9
    print('f(513553007) returns', sum_repeated_digits(513553007))  # 21
