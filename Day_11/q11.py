# Advent of Code 2024, Day 11 -> https://adventofcode.com/2024/day/11

# Given a list of engraved stones, use the AOC rules to translate to a new stone(s)
def transStones(lst):
    newEngravings = []
    for num in lst:
        if num == 0:
            newEngravings.append(1)
        # If even ammount of digits [casting to string to get length (number of digits)]
        elif len(str(num)) % 2 == 0:
            temp = str(num)                 # Convert to string so we can get the length of it
            mid = int(len(temp)/2)          # The mid integer is found by taking the length and dividing by 2
            left = temp[:mid]               # Left is defined as everything left of the mid index
            right = temp[mid:]              # Right is defined as everything right of the mid index
            newEngravings.append(int(left))
            newEngravings.append(int(right))
        else:
            newEngravings.append(num * 2024)
    return newEngravings

## Textfile and Driver function ##
file = open("input/q11.txt").read().split(' ')
input = []
for line in file:
    input.append(int(line))

## Grab the stone count after 25 blinks and store it in "ans1", do the same @ 75 blinks for "ans2" (Does not work, as brute force takes too much memory)
# for i in range(75):
#     input = transStones(input)
#     if i == 25:
#         ans1 = len(input)
# ans2 = len(input)

for i in range(25):
    input = transStones(input)
ans1 = len(input)

print("Number of stones after 25 blinks: ", ans1)
# print("Number of stones after 75 blinks: ", ans2)