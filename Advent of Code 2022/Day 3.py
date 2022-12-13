# Day 3 Advent of code

#read in the puzzle
test = [l.strip() for l in open('\\aoc\\input.txt')]

#read in the demo
demo = [l.strip() for l in open('\\aoc\\test.txt')]


import string
x = list(range(1, 53))
y = string.ascii_lowercase[0:26] + string.ascii_uppercase[0:26]

l = dict(zip(y, x))

use = test
#total part 1
t=0
#total part 2
t2=0

for i in range(len(use)):
    mid = int(len(use[i])/2)
    c = use[i][0:mid]
    d = use[i][mid:]
    t = t + [l[letter] for letter in c if l[letter] in set([l[let] for let in d])][0]

print(t)

#part 2 group by three and pop the common value into the running sum

group = int(len(use)/3)

for i in range(group):
    c = set([l[letter] for letter in use[3*i]])
    d = set([l[letter] for letter in use[3*i+1]])
    e = set([l[letter] for letter in use[3*i+2]])
    t2 = t2 + (c & d & e).pop()
print(t2)
