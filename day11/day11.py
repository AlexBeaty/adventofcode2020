# --- Day 11: Seating System ---

def get_data():
    with open('day11data.txt') as file:
        data = [list(line.strip()) for line in file]

        # append buffer for sliding window
        length = len(data[0])
        empties = list('.'*length)
        data.insert(0, empties)
        data.append(empties)
        data = [['.'] + line + ['.'] for line in data]
        return(data)


def get_neighbour_result(neighbours):
    seat = neighbours.pop(4)
    if seat == 'L':
        if neighbours.count('#') == 0:
            return('#')
    elif seat == '#':
        if neighbours.count('#') >= 4:
            return('L')

    return(seat)


def make_pass(data):
    new_data = [inner[:] for inner in data]
    for i in range(1, len(data)-1):
        # if i == 2:
        #     return(new_data)
        for j in range(1, len(data[i])-1):
            try:
                neighbours = [data[x][y] for x in range(i-1,i+2) for y in range(j-1,j+2)]
            except:
                print(f'{i},{j}')

            # print(data[i][j])    
            # print(f'nbrs: {neighbours}')
            new_data[i][j] = get_neighbour_result(neighbours)
            # print(data[i][j])
            # print()

    return(new_data)


if __name__ == '__main__':
    data = get_data()
    # data = [list('............'),
    #     list('.L.LL.LL.LL.'),
    #     list('.LLLLLLL.LL.'),
    #     list('.L.L.L..L...'),
    #     list('.LLLL.LL.LL.'),
    #     list('.L.LL.LL.LL.'),
    #     list('.L.LLLLL.LL.'),
    #     list('...L.L......'),
    #     list('.LLLLLLLLLL.'),
    #     list('.L.LLLLLL.L.'),
    #     list('.L.LLLLL.LL.'),
    #     list('............')
    #     ]

    # neighbours = [data[x][y] for y in range(1-1,1+2) for x in range(1-1,1+2)]
    # print(neighbours)
    # seat = neighbours.pop(4)
    # print(neighbours)

    # for line in data:
    #     print(line)
    
    # print('\n\n')
    while True:
        new_data = make_pass(data)

        if new_data == data:
            # print('final grid')
            # for lines in data:
            #     print(lines)   
            break

        data = new_data

    print(sum([line.count('#') for line in data])) 