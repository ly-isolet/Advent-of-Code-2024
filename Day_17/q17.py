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
                fileAsList.append(temp.split(": ")) # split each line into (register/program, value)
    # Check what register has what. Thankfully we only have a couple uniquely named registers so we can check naively
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

# given an operand code, return what bitwise function to preform
def decipherOperand(num):
    opFuncs = [adv, bxl, bst, jnz, bxc, out, bdv, cdv]
    return opFuncs[num]

# returns an integer, either the num or a value from a register, depending upon the rules of combo operands
def comboOperand(num, a, b, c):
    if num > 0 and num <= 3:
        return num
    elif num == 4:
        return a
    elif num == 5:
        return b
    elif num == 6:
        return c
    elif num == 7:
        print("7 found, invalid program")
        return -1
    else:
        print('ERROR: ', str(num), " not a valid combo")
        return -1
    
# given the function to do as a string (op), call the desired function
def doBitwise(op, rA, rB, rC, p, o):
    if op == 'adv':
        return adv(rA, rB, rC, p, o)
    if op == 'bxl':
        return bxl(rA, rB, rC, p, o)
    if op == 'bst':
        return bst(rA, rB, rC, p, o)
    if op == 'jnz':
        return jnz(rA, rB, rC, p, o)
    if op == 'bxc':
        return bxc(rA, rB, rC, p, o)
    if op == 'out':
        return out(rA, rB, rC, p, o)
    if op == 'bdv':
        return bdv(rA, rB, rC, p, o)
    if op == 'cdv':
        return cdv(rA, rB, rC, p, o)
    
# Preforms division of regA / 2 ** cOP --(truncated into int)--> regA 
def adv(a, b, c, p, o):    # opcode 0
    newA = int(a / 2 ** comboOperand(p[0]))
    return newA, b, c, p, o

# Preforms bitwise XOR of regB & litB -> regB
def bxl(a, b, c, p, o):    # opcode 1
    newB = b ^ 1
    return a, newB, c, p, o

# Preforms cOP % 8 -> regB
def bst(a, b, c, p, o):    # opcode 2
    newB = comboOperand(p[0]) % 8
    return a, newB, c, p, o

# If regA == 0: does nothing; otherwise jumps instructionPointer to litOP and DO NOT JUMP BY 2 AFTER INSTRUCTION
def jnz(a, b, c, p, o):    # opcode 3
    if a == 0:
        print("Doin' nuthin")
    else:
        insPntr = 3
        dontJump = True
    return a, b, c, p, o

# Preforms bitwise XOR of regB & regC -> regB
def bxc(a, b, c, p, o):    # opcode 4
    newB = b ^ c
    return a, newB, c, p, o

# OUTPUTS cOP % 8
def out(a, b, c, p, o):    # opcode 5
    o.append(comboOperand(p[0]))
    return a, b, c, p, o

# Preforms division of regA / 2 ^ cOP --(truncated into int)--> regB
def bdv(a, b, c, p, o):    # opcode 6
    newB = int(a / 2 ** comboOperand(p[0]))
    return a, newB, c, p, o

# Preforms division of regA / 2 ^ cOP --(truncated into int)--> regC
def cdv(a, b, c, p, o):    # opcode 7
    newC = int(a / 2 ** comboOperand(p[0]))
    return a, b, newC, p, o

## actually runs everything
def runProgram(a, b, c, p, o):
    insPntr = 0     # iterates by 2 (unless jump used)
    output = []
    dontJump = False

    for instr in p:
        newA, newB, newC, newP, newO = doBitwise(p[insPntr], a, b, c, p, o)
        output.append(newO)
        if dontJump == False:
            if len(p) <= 2:
                return  # reached end of program, HALT
            p = p[2:]
    return output

## Driver function
temp = []
rA, rB, rC, prog = parseFile('input/d17Test.txt')
ans1 = runProgram(rA, rB, rC, prog, temp)

print(ans1)
# print(rA,'\n',rB,'\n',rC,'\n',prog)