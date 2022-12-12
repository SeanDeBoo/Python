# Day 1 Advent of code

#read in the puzzle
test = [l.strip() for l in open('\\aoc\\input.txt')]

#read in the demo
demo = [l.strip() for l in open('\\aoc\\test.txt')]

use = test

# part 1
t=0
ans=[]
for i in range(len(use)):
    if use[i] != '':
        t = t + int(use[i])
    elif use[i] == '':
        ans.append(t)
        t = 0
ans.append(t)
print(max(ans))


# part 2
# print the end of the answers sorted from smallest to largest
ans = sorted(ans)
print(sum(ans[-3:]))
