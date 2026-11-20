# A program with a function that returns the acronym (the first letters of all words) of a text.


def acronym(name):
    result = ''
    # split() cuts the text into a list of words at the spaces
    for word in name.split():
        result = result + word[0]
    return result


if __name__ == "__main__":
    print('f("Internet of Things") returns', acronym("Internet of Things"))  # IoT
    print('f("For Your Information") returns', acronym("For Your Information"))  # FYI
    print('f("Python") returns', acronym("Python"))  # P
