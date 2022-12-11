import pandas as pd

test = pd.read_csv('q10.csv', sep=' ', header=None )
demo = pd.read_csv('demo.csv', sep=' ', header=None )

b = test.values.tolist() 
e = demo.values.tolist() 

b = [list(el) for el in b]
e = [list(string) for string in e]

keys = [20, 60, 100, 140, 180, 220]
points={}

demo=b

m = '#'

#cycle number is N
n=0
#current position of the sprite
X=1
for i in range(len(b)):
        if b[i][0]=='addx':
            n=n+2
            points[n-1]=X
            if X == ((n-1)%40) or X-1 == ((n-1)%40) or X+1== ((n-1)%40):
                    m=m+'#'
            else:
                    m=m+'.'
            X= X + int(b[i][1])
            points[n] = X
            if X == n%40 or X-1 == n%40 or X+1==n%40:
                    m=m+'#'
            else:
                    m=m+'.'
        elif b[i][0]=='noop':
            n=n+1
            points[n]=X    
            if X == n%40 or X-1 == n%40 or X+1==n%40:
                    m=m+'#'
            else:
                    m=m+'.'
ans = sum([points[key-1]*(key) for key in keys])
print(ans)

print(m[0:40])
print(m[40:80])
print(m[80:120])
print(m[120:160])
print(m[160:200])
print(m[200:240])
