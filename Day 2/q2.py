# Day 2 of Advent of Code 2024 -> https://adventofcode.com/2024/day/2

def isSafe(line):
    # These are all booleans, set to 1 for TRUE
    isIncreasing = 1
    isDecreasing = 1
    isWithinBounds = 1

    for i in range(len(line)-1):
        curr, nxt = int(line[i]), int(line[i+1])
        diff = abs(nxt - curr)
        
        isIncreasing = isIncreasing and (curr < nxt)
        isDecreasing = isDecreasing and (curr > nxt)
        isWithinBounds = isWithinBounds and (diff <= 3 and diff >= 1)

    return (isIncreasing or isDecreasing) and isWithinBounds

def isSafeRemoved(line):
    for i in range(len(line)):
        removed = line[:i] + line[i+1:]
        if isSafe(removed):
            return 1
    return 0

def isSafe2(line):
    return isSafe(line) or isSafeRemoved(line)

## Driver function ##
with open("Day 2/q2.txt", 'r') as file:
    lines = file.readlines()

ans1 = 0
ans2 = 0
for line in lines:
    ans1 += isSafe(line.split())
    ans2 += isSafe2(line.split())

print("Answer 1:", ans1)
print("Answer 2:", ans2)