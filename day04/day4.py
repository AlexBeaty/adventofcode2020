# --- Day 4: Passport Processing ---
import re

with open('day4data.txt') as file:
    data_string = file.read()
    data = data_string.split('\n\n')
    data = [line.replace('\n', ' ') for line in data]


def check_fields_weak(entry):
    entry_results = []
    fields = ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']

    for field in fields:
        entry_results.append(bool(re.search(field, entry)))

    # print(entry_results)
    return(True if all(entry_results) else False)

def check_fields_strong(entry):
    entry = entry.split()
    entry_dict = {}
    entry_results = []

    for field in entry:
        x = field.find(':')
        entry_dict[field[:x]] = field[x+1:]

    # byr
    try:
        byr = int(entry_dict['byr'])
        entry_results.append(byr >= 1920 and byr <= 2002)
    except:
        return(False)
    # iyr
    try:
        iyr = int(entry_dict['iyr'])
        entry_results.append(iyr >= 2010 and iyr <= 2020)
    except:
        return(False)
    # eyr
    try:
        eyr = int(entry_dict['eyr'])
        entry_results.append(eyr >= 2020 and eyr <= 2030)
    except:
        return(False)
    # hgt
    try:
        hgt = int(entry_dict['hgt'][:-2])
        unit = entry_dict['hgt'][-2:]
        entry_results.append((hgt >= 150 and hgt <= 193 and unit == 'cm') or (hgt >= 59 and hgt <= 76 and unit == 'in'))
    except:
        return(False)
    # hcl
    try:
        entry_results.append(bool(re.search('^#[a-f0-9]{6}$', entry_dict['hcl'])))
    except:
        return(False)
    # ecl
    try:
        entry_results.append(entry_dict['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth'])
    except:
        return(False)
    # pid
    try:
        entry_results.append(bool(re.search('^[0-9]{9}$', entry_dict['pid'])))
    except:
        return(False)

    # print(entry_results)
    return(True if all(entry_results) else False)




# part A
print(sum([check_fields_weak(entry) for entry in data]))

# part B
print(sum([check_fields_strong(entry) for entry in data]))
