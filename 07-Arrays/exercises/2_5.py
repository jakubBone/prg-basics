# A program that gives information about the seats in a cinema: total, available, booked and a seat status.

# 5x5 cinema seating
# A = Available, B = Booked
cinema_seats = [
    ['A', 'A', 'B', 'A', 'A'],
    ['A', 'B', 'B', 'A', 'A'],
    ['A', 'A', 'A', 'A', 'B'],
    ['B', 'A', 'A', 'A', 'A'],
    ['A', 'B', 'A', 'A', 'A']
]


def seats_total(seats):
    # the number of rows times the number of seats in the first row
    return len(seats) * len(seats[0])


def seats_available(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == 'A':
                count += 1
    return count


def seats_booked(seats):
    count = 0
    for row in seats:
        for seat in row:
            if seat == 'B':
                count += 1
    return count


def seat_status(seats, row, place):
    # rows and places are numbered from 1, the indexes from 0
    if seats[row - 1][place - 1] == 'A':
        return 'available'
    return 'booked'


print('CINEMA INFORMATION TABLE')
print('Total seats:', seats_total(cinema_seats))
print('Seats available:', seats_available(cinema_seats))
print('Seats booked:', seats_booked(cinema_seats))
print('Seat in row 1, place 1:', seat_status(cinema_seats, 1, 1))
print('Seat in row 5, place 5:', seat_status(cinema_seats, 5, 5))
print('Seat in row 3, place 5:', seat_status(cinema_seats, 3, 5))
