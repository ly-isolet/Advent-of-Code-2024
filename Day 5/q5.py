# Advent of Code 2024, Day 5 -> https://adventofcode.com/2024/day/5

# open file, splice file into two arrays: dictionary of rules(|), pages with updates(,)
# for each line of updates, figure out if it is valid or not. Retain only the valid updates.
# finally, find the middle page number in each validated page updates

from collections import defaultdict

rules = defaultdict(list)
updates = []
validUpdates = []
middles = []

file = open('Day 5/d5.txt').read().splitlines()

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

# for item in updates:
    
