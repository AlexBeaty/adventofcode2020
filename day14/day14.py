# --- Day 14: Docking Data ---
import re
import itertools

def get_instructions():
    with open('day14data.txt') as file:
        instructions = [line.strip() for line in file]
        return(instructions)


def get_addr_to_change(float_address):
    bit_strings = [''.join(seq) for seq in itertools.product('01', repeat=float_address.count('X'))]
    addr_to_change = []
    for bitty in bit_strings:
        temp_float_addr = float_address
        for bit in bitty:
            # asdf = temp_float_addr.find('X')
            temp_float_addr = temp_float_addr.replace('X', bit, 1)
            # print(f'{temp_float_addr}\nbit:{bit} insert at index:{asdf}\n')
        addr_to_change.append(temp_float_addr)
    return(addr_to_change)


def part_1(instructions):
    mask, mem = [], {}
    val = ['0' for _ in range(36)]
    addr = None
    for ins in instructions:
        if re.search('^mask', ins):
            mask = list(re.search('= (.+)', ins).group(1))
        else:
            components = re.search('^mem\[(\d+)\] = (\d+)', ins)
            addr = int(components.group(1))
            val = list(format(int(components.group(2)), '036b'))
        
            # apply mask to binary value and convert back to int
            masked_val = ''.join([v if m == 'X' else m for v,m in zip(val, mask)])
            val_int = int(masked_val, 2)

            # store masked value at address
            if addr is not None:
                mem[addr] = val_int

        # val_1 = ''.join(val)
        # mask_1 = ''.join(mask)
        # print(f'val: {val_1}\nmask: {mask_1}\nmasked_val: {masked_val}\nval_int: {val_int}\naddr: {addr}\n')

    return(sum(mem.values()))


def part_2(instructions):
    mask, mem = [], {}
    val = ['0' for _ in range(36)]
    addr = None
    for ins in instructions:
        if re.search('^mask', ins):
            mask = list(re.search('= (.+)', ins).group(1))
        else:
            components = re.search('^mem\[(\d+)\] = (\d+)', ins)
            addr = list(format(int(components.group(1)), '036b'))
            val = int(components.group(2))

            float_address = ''.join([m if m == 'X' or m == '1' else a for m,a in zip(mask, addr)])
            addr_to_change = get_addr_to_change(float_address)

            for addr in addr_to_change:
                mem[int(addr, 2)] = val

    return(sum(mem.values()))



if __name__ == '__main__':
    instructions = get_instructions()

    # Part A
    print(part_1(instructions))

    # Part B
    print(part_2(instructions))