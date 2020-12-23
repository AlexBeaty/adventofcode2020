# --- Day 5: Binary Boarding ---

with open('day5data.txt') as file:
    data = [[line[:7], line[7:].strip()] for line in file]


def get_row(row_string):
    i, j = 0, num_rows
    for x in row_string:
        mid = i + ((j-i)//2)
        if x == 'F':
            j = mid
        else:
            i = mid + 1
    #     print(f'i:{i}, j:{j}')
    # print(f'final row:{i}')
    return(i)


def get_seat(seat_string):
    i, j = 0, num_seats
    for x in seat_string:
        mid = i + ((j-i)//2)
        if x == 'L':
            j = mid
        else:
            i = mid + 1
    #     print(f'i:{i}, j:{j}')
    # print(f'final seat:{i}')
    return(i)


def get_seat_id(entry):
    row = get_row(entry[0])
    col = get_seat(entry[1])
    return( row * 8 + col)


num_rows, num_seats = 127, 7
# Part A
# print(max([get_seat_id(entry) for entry in data]))

# Part B
# A bit of a janky solution, I didn't really understand the question. When using this solution, the correct seat is the seat_id between the two printed seat_id numbers.
sorted_seats = sorted([get_seat_id(entry) for entry in data])
for i in range(1, len(sorted_seats)-2):
    if sorted_seats[i] - 1 != sorted_seats[i-1] or sorted_seats[i] + 1 != sorted_seats[i+1]:
        print(sorted_seats[i])
print('fin')