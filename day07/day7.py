# --- Day 7: Handy Haversacks ---
# Not my code

import re
from collections import defaultdict

bags = defaultdict(dict)
with open('day7data.txt') as lines:
    for l in lines:
        bag = re.match(r'(.*) bags contain', l).groups()[0]
        for count, b in re.findall(r'(\d+) (\w+ \w+) bag', l):
            bags[bag][b] = int(count)


def part1():
    answer = set()
    def search(color):
        for b in bags:
            if color in bags[b]:
                answer.add(b)
                search(b)
    search('shiny gold')
    return len(answer)


def part2():
    def search(bag):
        count = 1
        for s in bags[bag]:
            multiplier = bags[bag][s]
            count += multiplier * search(s)
        return count
    return search('shiny gold' ) - 1

print(part1())
print(part2())