# A program with a function that checks whether a string of digits is a valid binary number.


def is_binary(binary_number):
    # an empty string is not a binary number
    if len(binary_number) == 0:
        return False
    for char in binary_number:
        # every character must be 0 or 1
        if char != '0' and char != '1':
            return False
    return True


if __name__ == "__main__":
    print('f("101101") returns', is_binary("101101"))  # True
    print('f("1311a10100") returns', is_binary("1311a10100"))  # False
