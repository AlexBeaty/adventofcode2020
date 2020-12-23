# --- Day 9: Encoding Error ---

with open('day9data.txt') as file:
    data = [int(line.strip()) for line in file]


def valid_number(target, nums):
    comp = []
    for i in nums:
        if target - i in comp:
            return(True)
        else:
            comp.append(i)
    return(False)


def contiguous_nums(target, nums):
    for j in range(len(nums)-1):
        slide_total = []
        for k in range(j, len(nums)-1):
            slide_sum = sum(slide_total)
            if slide_sum == target:
                return(min(slide_total) + max(slide_total))
            elif slide_sum < target:
                slide_total.append(nums[k])
            elif slide_sum > target:
                break
    return('no valid contiguous set of nums')


if __name__ == "__main__":
    # Part A
    preamble = 25
    part_b_target, part_b_index = 0, 0
    for x in range(preamble, len(data)-1):
        if not valid_number(data[x], data[x-preamble:x]):
            part_b_target, part_b_index = data[x], x
            print(data[x])

    # Part B
    print(contiguous_nums(part_b_target, data[:part_b_index]))