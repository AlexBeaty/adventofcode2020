# --- Day 13: Shuttle Search ---

def get_inputs():
    with open('day13data.txt') as file:
        start_time = int(file.readline())
        buses = [bus for bus in file.readline().split(',')]
        return(start_time, buses)


def find_earliest_bus(start_time, buses):
    buses = [int(bus) for bus in buses if bus != 'x']
    x = start_time
    while True:
        for bus in buses:
            if x % bus == 0:
                return(x - start_time, bus)
        
        x += 1


def earliest_time_all_buses(buses):
    buses = [int(bus) if bus != 'x' else -1 for bus in buses]
    time, bus_index = 1, 0

    while True:
        buses_at_cur_time = [bus for bus in buses if time % bus == 0]
        # print(f'time:{time}, bus_ind:{bus_index}, valid_buses: {buses_at_cur_time}')
        if buses[bus_index] in buses_at_cur_time:
            bus_index += 1
        else:
            bus_index = 0
        
        if bus_index == len(buses):
            return(time - len(buses) + 1)

        time += 1


if __name__ == "__main__":
    start_time, buses = get_inputs()

    # Part A
    wait_time, earliest_bus = find_earliest_bus(start_time, buses)    
    print(wait_time * earliest_bus)

    # Part B - Works for small inputs, but can't handle big boys
    print(earliest_time_all_buses(buses))
