# Advent of Code 2024, Day 7 -> https://adventofcode.com/2024/day/7
# Make the right numbers equal the left numeber through some form of math (should only need add or multiply, as the number is never getting smaller right to left)

# 1. Split input into answer (left side) and numbers (right side)
# 2. search thru numbers to see if numbers can add or multiply (or both) to be the answer.
#   2b. brute force?

# Takes (file)name as input and returns the two sides of the equation as lists
def parseInput(name):
    file = open(name).read().splitlines()

    answers = []
    numbers = []
    # split the file input into two arrays to hold each side of the 'equation'
    for line in file:
        splitLine = line.split(': ')
        answers.append(splitLine[0])
        numbers.append(splitLine[1])
    
    return answers, numbers

# Recursion
def search(cur, rightside, leftside):
    if len(rightside) == 0:
        return cur == leftside
    if cur > leftside:
        return False
    temp = rightside[1:]
    ## p1
    return search(cur + rightside[0], temp, leftside) or search(cur * rightside[0], temp, leftside)
    ## p2
    # return search(cur + l[0], temp, target) or search(cur * l[0], temp, target) or search(int(str(cur) + str(l[0])), temp, target)



# Driver section!
total = 0
answers, numbers = parseInput('Day 7/q7.txt')
for i in range(len(answers)):
    answer = int(answers[i])
    number = numbers[i]
    if search(0, list(map(int, number.split(' '))), answer):
        total += answer
print(total)
