# Day 9

import pandas as pd
import numpy as np

demo = pd.read_csv(\\demo.csv', sep=' ', header=None )
test = pd.read_csv(\\q9.csv', sep=' ', header=None )

b = test.values.tolist() 
#b = demo.values.tolist() 

b = [list(string) for string in b]

demo=b
# tracker of positions visited for part 1 and 2                   
trackera={(0, 0)}
tracker={(0, 0)}
                   
# Function for tracking rope movements
def rope(n):
    if (h[n][1] - t[n][1]==-2 and h[n][0]-t[n][0]==0):
        t[n][1] = t[n][1]-1
    elif ((h[n][1] - t[n][1])==-2 and (abs(h[n][0]-t[n][0])))>=1:
        t[n][1] = t[n][1]-1
        t[n][0] = t[n][0]+int(abs(h[n][0]-t[n][0])/(h[n][0]-t[n][0]))
        #right
    elif ((h[n][1] - t[n][1])==2 and (h[n][0]-t[n][0])==0):
        t[n][1] = t[n][1]+1
    elif (h[n][1] - t[n][1])==2 and abs(h[n][0]-t[n][0])>=1:
        t[n][1] = t[n][1]+1
        t[n][0] = t[n][0]+int(abs(h[n][0]-t[n][0])/(h[n][0]-t[n][0]))
        #down
    elif ((h[n][0] - t[n][0])==-2) and (h[n][1]-t[n][1]==0):
        t[n][0] = t[n][0]-1
    elif (((h[n][0] - t[n][0])==-2) and abs(h[n][1]-t[n][1])>=1):
        t[n][1] = t[n][1]+int(abs(h[n][1]-t[n][1])/(h[n][1]-t[n][1]))
        t[n][0] = t[n][0]-1
        #up
    elif (((h[n][0]-t[n][0])==2) and h[n][1]-t[n][1]==0):
        t[n][0] = t[n][0]+1
    elif ((h[n][0]-t[n][0])==2 and abs(h[n][1]-t[n][1])>=1):
        t[n][1] = t[n][1]+int(abs(h[n][1]-t[n][1])/(h[n][1]-t[n][1]))
        t[n][0] = t[n][0]+1
    #next knot will be the current tail
    h[n+1]=t[n]

#Function for moving head of the rope                  
def move(demo):
        if demo == 'L':
            h[0][1] = h[0][1] - 1
        elif demo == 'R':
            h[0][1] = h[0][1] + 1
        #down
        elif demo == 'D':
            h[0][0] = h[0][0] - 1
        #up
        elif demo == 'U':
            h[0][0] = h[0][0] + 1

# [height, left/right ]
h= [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
t= [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

for i in range(len(demo)):
    for k in range(demo[i][1]):
            move(demo[i][0])
            for n in range(0,9):
               rope(n)
            tracker.add(tuple(h[9]))
            trackera.add(tuple(t[0]))
print('Answer for Part 1', len(trackera), 
      'And Part 2, 10th knot in the rope visits',
      len(tracker))
