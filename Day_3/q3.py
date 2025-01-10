#  Day 3 of Advent of Code 2024, https://adventofcode.com/2024/day/3
import re

file = open('input/q3.txt').read().splitlines()

ans1 = 0
ans2 = 0
disabled = False
for line in file:
    p1 = re.findall('mul\([0-9]+,[0-9]+\)', line)
    p2 = re.findall('(mul\([0-9]+,[0-9]+\))|(do\(\))|(don\'t\(\))', line)
    for i in p1:
        left, right = i.split(',')
        ans1 += int(left[4:]) * int(right[:-1])
    for j in p2:
        if j[1] != '':
            disabled = False
        elif j[2] != '':
            disabled = True
        elif not disabled:
            left, right = j[0].split(',')
            ans2 += int(left[4:]) * int(right[:-1])

print("Part 1 answer:", ans1, "\nPart 2 answer:", ans2)