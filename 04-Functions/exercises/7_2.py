# A program that shows the main() function and the __name__ == "__main__" construct.


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():
    # this code is executed only when the script is run directly
    x = 10
    y = 5
    print(f"Add: {add(x, y)}")
    print(f"Subtract: {subtract(x, y)}")


# __name__ is "__main__" only when the file is run directly, not when it is imported as a module
if __name__ == "__main__":
    main()
