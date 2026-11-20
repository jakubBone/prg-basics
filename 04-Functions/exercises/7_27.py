# A program with a function that checks a product code: three digits and a control digit.
# The control digit is the remainder of dividing the sum of the first three digits by 7.


def is_code_correct(product_code):
    if len(product_code) != 4 or not product_code.isdigit():
        return False
    digits_sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    control_digit = int(product_code[3])
    return digits_sum % 7 == control_digit


if __name__ == "__main__":
    print('f("1082") returns', is_code_correct("1082"))  # True
    print('f("2035") returns', is_code_correct("2035"))  # True
    print('f("1114") returns', is_code_correct("1114"))  # False
    print('f("7071") returns', is_code_correct("7071"))  # False
