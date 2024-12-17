# Advent of Code 2024, Day 17 -> https://adventofcode.com/2024/day/17
# 3-bit computer (bitwise functions)

# Takes input file and converts it into the values given for: register A, B, C, and the program
def parseFile(fname):
    fileAsList = []
    regA, regB, regC = 0, 0, 0
    program = ""
    with open(fname, 'r') as file:
        for line in file:
            if line != '\n':
                temp = line[:-1]                    # remove newline char
                fileAsList.append(temp.split(": ")) # split each line to make grabing values and checking which register more easily
    for i in fileAsList:
        if i[0].__contains__("A"):
            regA = int(i[1])
        if i[0].__contains__("B"):
            regB = int(i[1])
        if i[0].__contains__("C"):
            regC = int(i[1])
        if i[0].__contains__("P"):
            program = str(i[1])

    return regA, regB, regC, program

# Deciphers what is meant by the combo operand
def decipherCombo(int):
    op = []
    if int > 0 and int <= 3:
        op.append(int(int))
    elif int == 4:
        op.append('A')
    elif int == 5:
        op.append('B')
    elif int == 6:
        op.append('C')
    elif int == 7:
        print("7 found, invalid program")
    else:
        print('ERROR: ', str(int), " not a valid combo")
    
    return op   # either int or string depending on what the combo operand is

# Preforms division of regA / 2 ^ cOP --(truncated into int)--> regA 
def adv(a, b, c, p):    # opcode 0
    reg

# Preforms bitwise XOR of regB & litB -> regB
def bxl(a, b, c, p):    # opcode 1
    TODO

# Preforms cOP % 8 -> regB
def bst(a, b, c, p):    # opcode 2
    TODO

# If regA == 0: does nothing; otherwise jumps instructionPointer to litOP and DO NOT JUMP BY 2 AFTER INSTRUCTION
def jnz(a, b, c, p):    # opcode 3
    TODO

# Preforms bitwise XOR of regB & regC -> regB
def bxc(a, b, c, p):    # opcode 4
    TODO

# OUTPUTS cOP % 8
def out(a, b, c, p):    # opcode 5
    TODO

# Preforms division of regA / 2 ^ cOP --(truncated into int)--> regB
def bdv(a, b, c, p):    # opcode 6
    TODO

# Preforms division of regA / 2 ^ cOP --(truncated into int)--> regC
def cdv(a, b, c, p):    # opcode 7
    TODO

## Driver function
insPntr = 0     # iterates by 2 (unless jump used)

rA, rB, rC, prog = parseFile('Day 17/test.txt')
