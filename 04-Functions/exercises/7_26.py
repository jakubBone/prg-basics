# A program with a function that returns a text with all characters separated by a dash.


def with_dashes(text):
    result = ''
    for i in range(len(text)):
        # a dash is added before every character except the first one
        if i > 0:
            result = result + '-'
        result = result + text[i]
    return result


if __name__ == "__main__":
    print('f("University") returns', with_dashes("University"))  # U-n-i-v-e-r-s-i-t-y
    print('f("UE") returns', with_dashes("UE"))  # U-E
    print('f("x") returns', with_dashes("x"))  # x
    print('f("") returns', repr(with_dashes("")))  # ''
