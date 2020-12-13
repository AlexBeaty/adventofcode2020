# --- Day 3: Toboggan Trajectory ---

with open('day3data.txt') as file:
    data = [line.strip() for line in file]

def tree_encounters(mv_x, mv_y):
    width = len(data[0])
    x, y = 0, 0
    trees = 0

    while y < len(data):
        # print(f'y:{y}, x:{x}')

        if data[y][x] == '#':
            trees += 1

        x = (x + mv_x) % width
        y += mv_y

    return(trees)

# part a

# print(tree_encounters(3,1))

# part b

inputs = [(1,1),(3,1),(5,1),(7,1),(1,2)]
trees_multiplied = 1
for x,y in inputs:
    trees_multiplied *= tree_encounters(x,y)

print(trees_multiplied)