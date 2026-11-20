# A program with a function that checks whether an expression is a palindrome (reads the same backwards).


def is_palindrome(palindrome):
    # compare the first character with the last, the second with the second from the end, and so on
    length = len(palindrome)
    for i in range(length // 2):
        if palindrome[i] != palindrome[length - 1 - i]:
            return False
    return True


if __name__ == "__main__":
    print('f("radar") returns', is_palindrome("radar"))  # True
    print('f("12-11-21") returns', is_palindrome("12-11-21"))  # True
    print('f("book") returns', is_palindrome("book"))  # False
