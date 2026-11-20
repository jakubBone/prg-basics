# A program with a function that checks whether at least 3 people were in the room at the same time.
# The sign + is a person entering, the sign - is a person leaving.


def three_people_at_once(detector):
    people = 0
    max_people = 0
    for sign in detector:
        if sign == '+':
            people += 1
        else:
            people -= 1
        # remember the biggest number of people in the room so far
        if people > max_people:
            max_people = people
    return max_people >= 3


if __name__ == "__main__":
    print('f("+-+++-+---") returns', three_people_at_once("+-+++-+---"))  # True
    print('f("+-+-+-+-") returns', three_people_at_once("+-+-+-+-"))  # False
    print('f("+-++-+--") returns', three_people_at_once("+-++-+--"))  # False
    print('f("+-++-++-+---") returns', three_people_at_once("+-++-++-+---"))  # True
