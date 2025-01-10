# Advent of Code 2024, Day 4 -> https://adventofcode.com/2024/day/4
# Word search (path tracing)

### Variables
directions = [(-1,1),(1,1),(1,-1),(-1,-1),(1,0),(0,1),(-1,0),(0,-1)]
XMAS = 'XMAS'

### Functions
# Takes input and slots it into a matrix with dimensions (length of line) x (length of file), returns the completed matrix and the number of rows / columns
def parseFile(fname):
    with open(fname,'r') as file:
        lines = file.readlines()

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
    return row < 0 or row >= rows or col < 0 or col >= cols

# checks if 'XMAS' can be created if given direction, row, and column
def check1(row, col, dir):
    for i in range(4):               # 'XMAS' is four letters, hence 4 steps
        nextRow = row + dir[0] * i   # the next row to check is in the specified direction * the number of jumps we need to get there
        nextCol = col + dir[1] * i   # same as above just with the column 
    # check out of bounds, then check if it's the correct letter
        if isOutOfBounds(nextRow, nextCol) or wordSearch[nextRow][nextCol] != XMAS[i]:
            return False
    return True

# check if 'MAS' can be found in an 'X' pattern
def check2(row, col):
    if not 0 < row < rows - 1 or not 0 < col < cols - 1 or wordSearch[row][col] != 'A':
        return False
    # create an array of the letters to the bottom left, bottom right, top left, and top right right characters (should be 'M' and 'S')
    chars = [wordSearch[row-1][col-1], wordSearch[row-1][col+1], wordSearch[row+1][col-1], wordSearch[row+1][col+1]]
    # There should be 2 of each 'M' and 'S' if 'MAS' can be found in an X pattern
    m, s = len(list(filter(lambda x: x == 'M', chars))), len(list(filter(lambda x: x == 'S', chars)))
    if m == s == 2:
        return wordSearch[row-1][col-1] != wordSearch[row+1][col+1] 

def part1():
    numFound = 0
    for r in range(rows):
        for c in range(cols):
            if wordSearch[r][c] == 'X':    
                for d in directions:
                    if check1(r, c, d):
                        numFound += 1   # 'XMAS' can be found
    print("Part 1:", numFound)

def part2():
    numFound = 0
    for r in range(1, len(wordSearch) - 1):
        for c in range(1, len(wordSearch[0]) - 1):
            if check2(r, c):
                numFound += 1   # 'MAS' can be found in an 'X' pattern
    print("Part 2:", numFound)

### Driver section
wordSearch = (parseFile("input/q4.txt"))
rows = len(wordSearch)
cols = len(wordSearch[0])

part1()
part2()