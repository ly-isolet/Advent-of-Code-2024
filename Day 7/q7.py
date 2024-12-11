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
        splitLine = line.split(':')
        answers.append(splitLine[0])
        numbers.append(splitLine[1])
    
    return answers, numbers

# Takes two list[int] and calculates if the right side numbers can combine (add / mult) to equal the left number 
def mathMoment(leftside, rightside):
    # valids = []
    totalValid = 0

    for num in leftside:
        isValid = False
        ## CONTINUE HERE ##
        
    return totalValid



# Driver section!
parsedInput = parseInput('Day 7/d7.txt')
validEquations = mathMoment(parsedInput[0], parsedInput[1])
total = len(validEquations)

# print(total)