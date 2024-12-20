# Advent of Code 2024, Day 5 -> https://adventofcode.com/2024/day/5

# open file, splice file into two arrays: dictionary of rules(|), pages with updates(,)
# for each line of updates, figure out if it is valid or not. Retain only the valid updates.
# finally, find the middle page number in each validated page updates
from collections import defaultdict
from math import floor

def parseFile(fname):
    rules = defaultdict(list)
    updates = []
    pages = []

    file = open(fname).read().splitlines()
    for line in file:
        # Notice all rules follow the syntax: double-digit numer | double-digit number ; Therefore the length of all rules will be 5
        if len(line) == 5:
            # Separate each rule into its left and right pages and add them to the dictionary
            separatedNums = line.split('|')
            leftPage = separatedNums[0]
            rightPage = separatedNums[1]
            rules[leftPage].append(rightPage)   # Note: this makes it so each key (left page) has a list value associated it (multiple pages), this is done to avoid dictionaries not allowing duplicates
                                                # ex: '56' : ['67', '68', '47', '59', '18', '87', '46', '27', '32', '43', ...]
        # Aside from the empty line, the rest of the file's contents should be a list of page updates
        elif len(line) != 0:
            updates.append(line)
    for update in updates:
        pages.append(update.split(','))

    return rules, pages

# Checks to see if the given pages to update are valid
def isValid(pages):
    for i in range(len(pages) - 1):                         # for the length of pages (-1 bc arr start @ 0)
        for j in range(i + 1, len(pages)):                  # starting at 1
            if not rules[pages[i]].__contains__(pages[j]):  # if the given page does not follow the rules for its page number, retrun False
                return False
    return True

# swaps pages based upon rules
def swap(pages):
    i = 0
    while i < len(pages) - 1:
        j = i +1
        while j < len(pages):
            # if rules not followed swap earlier page with following page
            if not rules[pages[i]].__contains__(pages[j]): # same logic as isValid
                temp = pages[j]
                pages[j] = pages[i]
                pages[i] = temp
            # otherwise continue the loop
            else:
                j += 1
        i += 1

## Driver code
ans1 = 0
ans2 = 0
rules, pages = parseFile('Day 5/q5.txt')
for p in pages:
    if not isValid(p):  # if not valid use swap method to make it valid
        swap(p)
        ans2 += int(p[floor(len(p) / 2)])
    else:               # if valid, grab the value at the middle page, cast it to an int and add it to ans1
        ans1 += int(p[floor(len(p) / 2)])

print("Part 1: ", ans1)
print("Part 2: ", ans2)