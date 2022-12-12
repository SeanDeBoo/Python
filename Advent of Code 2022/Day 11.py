import pandas as pd
from math import trunc

test = pd.read_csv('q11.csv', header=None )
#demo = pd.read_csv('demo.csv', header=None )

b = test.values.tolist() 
#b = demo.values.tolist() 

b = [list(el) for el in b]

#Dictionaties to track movement of items
y = {}
T=[]
path = {}
rule={}

#count for monkey analysis
m=[0,0,0,0,0,0,0,0]

def change(level, rule):
    if rule[0] == '*' and rule[1]=='old':
        level = trunc((int(level) * int(level)))
        return(level)
    elif rule[0] == '*':
        level = trunc((int(level) * int(rule[1])))
        return(level)
    elif rule[0] == '+':
        level = trunc((int(level) + int(rule[1])))
        return(level)
    

#build the rule book
for i in range(0 , int(len(b)/6)):
    #build inventory
    y[b[i*6][0].split(':')[0].split(' ')[1]] = b[1+i*6][0].split(':')[-1].split(',')
    #build operation
    rule[i] = b[2+i*6][0].split(' ')[-2:]
    # Test value
    T.append(b[3+i*6][0].split(' ')[-1])
    #path
    path[i] = (int(b[4+i*6][0].split(' ')[-1]), int(b[5+i*6][0].split(' ')[-1]))

supermod=1
supermods = [int(el) for el in T]
for h in range(len(supermods)):
    supermod = supermod*supermods[h] 

# for part A, divide by 3 instead of supermod

print(y)    
#run a loop through the system
for i in range(0,10000):
    for j in range(int(len(b)/6)):
        y[str(j)].reverse()
        for k in range(len(y[str(j)])):
            y[str(j)][-1] = change(y[str(j)][-1], rule[j]) % supermod
            if int(y[str(j)][-1]) % int(T[j]) != 0:
                m[j]  = m[j]+1
                y[str(path[j][1])].append(y[str(j)].pop())
            elif int(y[str(j)][-1]) % int(T[j]) == 0:
                m[j]  = m[j]+1
                y[str(path[j][0])].append(y[str(j)].pop())

m = sorted(m)
ans = m[-1]*m[-2]
print(ans)
