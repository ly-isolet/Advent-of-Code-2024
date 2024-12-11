# Day 1 of Advent of Code 2024 -> https://adventofcode.com/2024/day/1
from collections import defaultdict

a1 = []
a2 = []

with open("Day 1/q1.txt", "r") as file:
    lines = file.readlines()
    a2Freq = defaultdict(int)

    for line in lines:
        nums = line.split()         # Use split to separate left and right side of input
        a1.append(int(nums[0]))     # a1 gets left side
        a2.append(int(nums[1]))     # a2 gets right side
        a2Freq[int(nums[1])] += 1   # a2Freq incriments to show how often a number appears in the right side
    
    # Lists must be organized smallest to largest so we use the built in sort() funciton on both a1 & a2
    a1.sort()
    a2.sort()

    ans1 = 0
    ans2 = 0
    # Use length of a1 as both a1 & a2 should be equal in length
    for i in range(len(a1)):
        ans1 += abs(a1[i] - a2[i])      # Use subtraction and widow in order to find 'distance' between numbers
        ans2 += a1[i] * a2Freq[a1[i]]   # Part 2 stipulates we multiply the left list number by the frequency of that number in the right list
    
    print('Part 1 answer:', ans1)
    print('Part 2 answer:', ans2)