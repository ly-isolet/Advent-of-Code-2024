#  Day 3 of Advent of Code 2024, https://adventofcode.com/2024/day/3

def mul(a, b) -> int:
    return (a * b)

file = open('Day 3/q3.txt').read().splitlines()

correct = False # Boolean to hold if we are in correct format up until this point
total = 0

# for line in file:
