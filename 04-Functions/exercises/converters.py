# Functions for converting length units (a copy of converters.py extended with two new functions).

def m_to_cm(n):
    return n*100


def cm_to_m(n):
    return n/100


def cm_to_inch(cm):
    # 1 inch = 2.54 cm
    return cm / 2.54


def feet_inches_to_cm(feet, inches):
    # 1 foot = 12 inches, so everything is first changed to inches
    return (feet * 12 + inches) * 2.54


if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'254cm = {cm_to_inch(254)} inches')
    print(f'5 feet 7 inches = {feet_inches_to_cm(5, 7)}cm')
