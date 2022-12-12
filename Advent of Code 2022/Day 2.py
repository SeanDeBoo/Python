# Day 2 Advent of code

#read in the puzzle
test = [l.strip().split(' ') for l in open('\\aoc\\input.txt')]

#read in the demo
demo = [l.strip().split(' ') for l in open('\\aoc\\test.txt')]

use = test

# part 1 look up values for the moves
move = {('A', 'X'): 4, ('A', 'Y'): 8, ('A', 'Z'): 3,
        ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
        ('C', 'X'): 7, ('C', 'Y'): 2, ('C', 'Z'): 6}

#play though the moves
t = 0
for elf, me in use:
    t = t + move[(elf, me)]
print(t)

# part 2 

# part 1 look up values for the moves
move2 = {('A', 'X'): 3, ('A', 'Y'): 4, ('A', 'Z'): 8,
        ('B', 'X'): 1, ('B', 'Y'): 5, ('B', 'Z'): 9,
        ('C', 'X'): 2, ('C', 'Y'): 6, ('C', 'Z'): 7}

#play though the moves
t = 0
for elf, me in use:
    t = t + move2[(elf, me)]
print(t)
