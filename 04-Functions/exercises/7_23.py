# A program with a function that checks a password: at least six characters, each character only once.


def is_password_valid(password):
    if len(password) < 6:
        return False
    for char in password:
        # if a character appears more than once, the password is not correct
        if password.count(char) > 1:
            return False
    return True


if __name__ == "__main__":
    print('f("ax15") returns', is_password_valid("ax15"))  # False
    print('f("book123") returns', is_password_valid("book123"))  # False
    print('f("A2water3") returns', is_password_valid("A2water3"))  # True
    print('f("qwerty") returns', is_password_valid("qwerty"))  # True
    print('f("") returns', is_password_valid(""))  # False
