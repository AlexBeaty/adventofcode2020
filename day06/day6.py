# --- Day 6: Custom Customs ---

with open('day6data.txt') as file:
    data = file.read()
    data = data.split('\n\n')
    data = [line.replace('\n', ' ').split(' ') for line in data]


def get_count_for_group(entry):
    comb_ans = ''.join(entry)
    return(len(set(comb_ans)))


def get_mutual_ans(entry):
    comb_ans, mut_ans = ''.join(entry), []  
    for l in comb_ans:
        if comb_ans.count(l) == len(entry) and l not in mut_ans:
            mut_ans.append(l)
    return(len(mut_ans))


# Part A
# print(sum([get_count_for_group(entry) for entry in data]))

# Part B
print(sum([get_mutual_ans(entry) for entry in data]))