# --- Day 10: Adapter Array ---

with open('day10data.txt') as file:
    data = [int(line.strip()) for line in file]


def count_diffs(nums):
    diff_1, diff_3 = 0, 0
    for x in range(1, len(nums)):
        temp_diff = nums[x] - nums[x-1]
        if temp_diff == 1:
            diff_1 += 1
        elif temp_diff ==3:
            diff_3 += 1
        else:
            print(f'diff of: {temp_diff}')
    return(diff_1 * diff_3)


def different_arrangements():
    # not my solution, dynamic programming or something?
    with open("day10data.txt") as f:
        rows = [int(r) for r in f.read().split("\n")]

    last = max(rows)
    index = [1] + [0] * last + [0, 0]
    for r in sorted(rows):
        index[r] = index[r-1] + index[r-2] + index[r-3]
        if r == last:
            print(f"{r=} {index[r]=}")
            break


if __name__ == '__main__':
    data.extend([0, max(data)+3])
    data.sort()
    # Part A
    print(count_diffs(data))
    # Part B
    different_arrangements()