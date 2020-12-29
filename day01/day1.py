# --- Day 1: Report Repair ---

# get data into list of ints
def get_data():
    with open('day1data.txt') as file:
        data = [int(i) for i in file]
        return(data)

# function to reduce tuple of ints to their combined product
def mult_reducer(items):
    if not items:
        return()
    total = 1
    for item in items:
        total *= item
    return(total)

# loop to check if target - current int exists in list: return their multiplication, otherwise add current to list and move on
def two_sum(tar, data):
    seen = []

    for cur in data:    
        if tar - cur in seen:
            # print(f'cur:{cur}, complement:{tar - cur}, ans:{cur*(tar-cur)}')
            return(cur, tar - cur)
        else:
            seen.append(cur)
    return(0)

# three sum function that feeds each permitation to two_sum()
def three_sum(tar, data):
    for i in range(len(data)):
        data_copy = data.copy()
        del data_copy[i]
        two_sum_res = two_sum(tar-data[i], data_copy)
        if two_sum_res != 0:
            return(data[i], two_sum_res[0], two_sum_res[1])
    return(f'no three sum combination for target:{tar}')


if __name__ == '__main__':
    data = get_data()

    ans1 = two_sum(2020, data)
    print(f'items:{ans1}, product:{mult_reducer(ans1)}')
    ans2 = three_sum(2020, data)
    print(f'items:{ans2}, product:{mult_reducer(ans2)}')
