# --- Day 8: Handheld Halting ---

with open('day8data.txt') as file:
    commands = [line.strip().split() for line in file]


def run_commands(commands):
    acc = 0
    i = 0
    seen_i = []
    print(f'acc before: {acc}')
    while True:
        seen_i.append(i)
        # i += read_command(commands[i])

        action = commands[i][0]
        value = commands[i][1]
        if action == 'acc':
            acc += int(value)
            i += 1
        elif action == 'nop':
            i += 1
        elif action == 'jmp':
            i += int(value)


        if i in seen_i:
            print('i already seen')
            # print(i)
            # print(seen_i)
            # return(False)
            break
        
        if i < 0:
            print('i less than 0')
            # return(False)
            break

        if i > len(commands) - 1:
            print('finished commands')
            break
    print(f'acc after: {acc}')
    return(acc)


# def read_command(command):
#     global acc
#     # print(command)
    


def change_commands(commands):
    for x in range(len(commands)-1):
        new_commands = commands.copy()
        if commands[x][0] == 'nop':
            new_commands[x][0] = 'jmp'
            print(run_commands(new_commands))
        elif commands[x][0] == 'jmp':
            new_commands[x][0] = 'nop'
            print(run_commands(new_commands))
    return(False)
        


# Part A
# print(commands[102])
# commands[102][0] = 'nop'
# print(commands[102])
# run_commands(commands)
# print(acc)

# Part B
# print(acc if change_commands(commands) else 'No valid command set found')
change_commands(commands)