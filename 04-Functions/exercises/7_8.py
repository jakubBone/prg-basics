# A program with a function that returns the minimum number of 1, 2 and 5 PLN coins needed to pay a given amount.


def min_coins(amount_to_pay):
    coins_5 = amount_to_pay // 5
    rest = amount_to_pay % 5
    coins_2 = rest // 2
    coins_1 = rest % 2
    return coins_5 + coins_2 + coins_1


if __name__ == "__main__":
    print('f(23) returns', min_coins(23))  # 6
    print('f(8) returns', min_coins(8))  # 3
    print('f(2) returns', min_coins(2))  # 1
    print('f(0) returns', min_coins(0))  # 0
