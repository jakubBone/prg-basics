# A program with a function that returns the dice number rolled the most times in a row.


def longest_series(dice):
    best_digit = ''
    best_length = 0
    current_length = 0
    previous = ''
    for char in dice:
        if char == previous:
            current_length += 1
        else:
            current_length = 1
        previous = char
        # a longer series replaces the best one found so far
        if current_length > best_length:
            best_length = current_length
            best_digit = char
    return int(best_digit)


if __name__ == "__main__":
    print('f("5233165554211") returns', longest_series("5233165554211"))  # 5
    print('f("2133") returns', longest_series("2133"))  # 3
