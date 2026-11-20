# A program with a function that returns a sentence with the spaces removed.


def remove_spaces(sentence):
    # replace(old, new) returns a new string in which every old text is replaced with the new one
    return sentence.replace(' ', '')


if __name__ == "__main__":
    print(remove_spaces("integrated development environment"))
    print(remove_spaces("A programming language is a system of notation for writing computer programs"))
