# --- Day 2: Password Philosophy ---

with open('day2data.txt') as data_raw:
    data = [line.strip().split() for line in data_raw]

def check_positions(line):
    range_split = line[0].find('-')
    range_lower, range_upper = int(line[0][0:range_split]), int(line[0][range_split+1:])

    pos1 = line[2][range_lower-1] == line[1][0]
    pos2 = line[2][range_upper-1] == line[1][0]

    return((pos1 or pos2) and not(pos1 and pos2))

print(sum([check_positions(line) for line in data]))