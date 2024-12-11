# Advent of Code 2024, Day 11 -> https://adventofcode.com/2024/day/11

def getDigitCount(number):
    return len(str(number))

# Given an engraved number, use the AOC rules to translate to a new stone(s)
def transStones(lst):
    newEngravings = []
    for num in lst:
        if num == 0:
            newEngravings.append(1)

        # If even ammount of digits
        elif getDigitCount(num) % 2 == 0:
            temp = str(num)                 # Convert to string so we can get the length of it
            mid = int(len(temp)/2)          # The mid integer is found by taking the length and dividing by 2
            left = temp[:mid]               # Left is defined as everything left of the mid index
            right = temp[mid:]              # Right is defined as everything right of the mid index
            newEngravings.append(int(left))
            newEngravings.append(int(right))

        else:
            newEngravings.append(num * 2024)

    return newEngravings

### TODO: Fix whatever is wrong with my text file code ###
# Textfile and Driver function ##
# file = open("Day 11/q11.txt").read().split()
# input = []
# for item in file:
#     input.append(int(item))
# for i in range(25): # 25 blinks
#     input = transStones(input)
# ans1 = len(input)
# print(ans1)

input = [3028, 78, 973951, 5146801, 5, 0, 23533, 857]
# Grab the stone count after 25 blinks and store it in "ans1", do the same @ 75 blinks for "ans2"
for i in range(75):
    input = transStones(input)
    if i == 25:
        ans1 = len(input)
ans2 = len(input)


print("Number of stones after 25 blinks: ", ans1)
print("Number of stones after 75 blinks: ", ans2)