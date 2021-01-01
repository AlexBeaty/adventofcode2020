# --- Day 15: Rambunctious Recitation ---
from tqdm import tqdm

def start_seq():
    with open('day15data.txt') as file:
        seq, turn, cur_num = {}, 1, None
        for num in file.readline().split(','):
            try:
                seq[int(num)].append(turn)
            except:
                seq[int(num)] = [turn]
                
            turn += 1
            cur_num = int(num)
        return(seq, turn, cur_num)


def get_next_num(seq, cur_num):
    prev_instances = seq[cur_num]
    if len(prev_instances) == 1:
        return(0)
    else:
        prev_instances.sort()
        return(prev_instances[-1] - prev_instances[-2])

if __name__ == '__main__':
    seq, turn, cur_num = start_seq()
    nth_num = 2020
    pbar = tqdm(total = nth_num)

    while True:
        # print(f'{seq}, {turn}, {cur_num}')
        next_num = get_next_num(seq, cur_num)
        try:
            seq[next_num].append(turn)
        except:
            seq[next_num] = [turn]
        cur_num = next_num

        if turn%1000 == 0:
            pbar.update(1000)

        if turn == nth_num:
            print(cur_num)
            break

        turn += 1
    
    pbar.close()
