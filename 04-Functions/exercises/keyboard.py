# Functions that read data of different types from the keyboard.

def input_string(message):
    text = input(message)
    return text


def input_integer(message):
    # input() always returns a string, so it is converted to int
    number = int(input(message))
    return number


def input_real(message):
    number = float(input(message))
    return number


def input_boolean(message):
    # the answer 'y' means True, any other answer means False
    answer = input(message)
    return answer == 'y'
