# --- Day 12: Rain Risk ---

def get_instructions():
    with open('day12data.txt') as file:
        data = [[line[0], int(line[1:].strip())] for line in file]
        return(data)


def get_new_fac(dir, val, fac):
    r_dir = {0:1,
            1:2,
            2:3,
            3:0}

    l_dir = {0:3,
            3:2,
            2:1,
            1:0}

    for x in range(val//90):
        if dir == 'L':
            fac = l_dir[fac]
        elif dir == 'R':
            fac = r_dir[fac]
        else:
            print('bad dir')

    return(fac)


if __name__ == '__main__':
    data = get_instructions()
    
    # Part A
    x_loc, y_loc, fac = 0, 0, 1
    # data = [['F', 10], ['N', 3], ['F', 7], ['R', 90], ['F', 11]]

    print(f'x:{x_loc}, y:{y_loc}, fac:{fac}')
    for op in data:
        if op[0] == 'L' or op[0] == 'R':
            fac = get_new_fac(op[0], op[1], fac)
        elif op[0] == 'F':
            if fac == 0:
                y_loc += op[1]
            elif fac == 1:
                x_loc += op[1]
            elif fac == 2:
                y_loc -= op[1]
            elif fac == 3:
                x_loc -= op[1]
            else:
                pass
        else:
            if op[0] == 'N':
                y_loc += op[1]
            elif op[0] == 'E':
                x_loc += op[1]
            elif op[0] == 'S':
                y_loc -= op[1]
            elif op[0] == 'W':
                x_loc -= op[1]
            else:
                pass

        print(f'x:{x_loc}, y:{y_loc}, fac:{fac}')
        
    # manhattan distance
    print(abs(x_loc) + abs(y_loc))

    # Part B
    ship_x, ship_y = 0, 0
    way_x, way_y = 10, 1

    for ops in data:
        way_diff_x, way_diff_y = way_x - ship_x, way_y - ship_y
        # move ship and way
        if ops[0] == 'F':
            for i in range(ops[1]):
                ship_x, ship_y = way_x, way_y
                way_x, way_y = ship_x + way_diff_x, ship_y + way_diff_y
        # rotate way cc
        elif ops[0] == 'L':
            for i in range(ops[1]//90):
                way_diff_x, way_diff_y = way_x - ship_x, way_y - ship_y
                way_x, way_y = ship_x - way_diff_y, ship_y + way_diff_x
        # rotate way c
        elif ops[0] == 'R':
            for j in range(ops[1]//90):
                way_diff_x, way_diff_y = way_x - ship_x, way_y - ship_y
                way_x, way_y = ship_x + way_diff_y, ship_y - way_diff_x
        elif ops[0] == 'N':
            way_y += ops[1]
        elif ops[0] == 'E':
            way_x += ops[1]
        elif ops[0] == 'S':
            way_y -= ops[1]
        elif ops[0] == 'W':
            way_x -= ops[1]
        else:
            pass
        print(f'ship: ({ship_x},{ship_y})    way:({way_x},{way_y})     inst:{ops}')

    print(abs(ship_x) + abs(ship_y))