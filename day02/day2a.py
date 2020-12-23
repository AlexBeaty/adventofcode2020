# --- Day 2: Password Philosophy ---

with open('day2data.txt') as data_raw:
    data = [line.strip().split() for line in data_raw]

def check_password(line):
    range_split = line[0].find('-')
    range_lower, range_upper = int(line[0][0:range_split]), int(line[0][range_split+1:])

    if line[2].count(line[1][0]) >= range_lower and line[2].count(line[1][0]) <= range_upper:
        return(True)
    else:
        return(False)



print(sum([check_password(line) for line in data]))