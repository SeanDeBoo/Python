# Day 4 Advent of code

#read in the puzzle
test = [l.strip().split(',') for l in open('\\aoc\\input.txt')]

#read in the demo
demo = [l.strip().split(',') for l in open('\\aoc\\test.txt')]


use = test
t=0
t2=0
# part 1 and 2 combined
for i in range(len(use)):
    a, b = map(int, use[i][0].split('-'))
    x, y = map(int, use[i][1].split('-'))
    if (x >= a and y <= b) or (a >= x and b <= y ):
        t=t+1
    if (a <= y and b >= x) or (x <= b and y >= a):
        t2=t2+1
        
print(t , t2)
