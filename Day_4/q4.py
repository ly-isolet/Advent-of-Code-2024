# Advent of Code 2024, Day 4 -> https://adventofcode.com/2024/day/4
# Word search (path tracing)

### Variables
directions = [(-1,1),(1,1),(1,-1),(-1,-1),(1,0),(0,1),(-1,0),(0,-1)]
XMAS = 'XMAS'
numFound = 0

### Functions
# Takes input and slots it into a matrix with dimensions (length of line) x (length of file), returns the completed matrix and the number of rows / columns
def parseFile(fname):
    with open(fname,'r') as file:
        lines = file.readlines()
    
    # Define the number of rows and cols to create the wordsearch
    # rows = len(lines)
    # columns = len(lines[0])
    grid = []

    # For each line in the file, append each char into a list, then append that list into the matrix (rather than 1 by 1)
    for line in lines:
        chars = []
        for c in line:
            if c != '\n':
                chars.append(c)
        grid.append(chars)

    return grid

# Checks if the next row or columns is out of bounds
def isOutOfBounds(row, col):
    # return row < 0 or row > len(wordSearch) or col < 0 or col > len(wordSearch[0])
    return row < 0 or row >= len(wordSearch) or col < 0 or col >= len(wordSearch[0])

# checks if xmas can be created if given direction, row, and column
def check(row, col, dir):
    for i in range(4):               # 'XMAS' is four letters, hence 4 steps
        nextRow = row + dir[0] * i   # the next row to check is in the specified direction * the number of jumps we need to get there
        nextCol = col + dir[1] * i   # same as above just with the column 
    # check out of bounds, then check if it's the correct letter
        if isOutOfBounds(nextRow, nextCol) or wordSearch[nextRow][nextCol] != XMAS[i]:
            return False
    return True

### Driver section
# wordSearch = (parseFile("input/q4.txt"))   # P1 Test should find 18 XMAS
wordSearch = (parseFile("input/d4P2Test.txt"))
rows = len(wordSearch)
cols = len(wordSearch[0])

for r in range(rows):
    for c in range(cols):
        if wordSearch[r][c] == 'X':    
            for d in directions:
                if check(r, c, d):
                    numFound += 1   # 'XMAS' can be found
print("Part 1: ", numFound)