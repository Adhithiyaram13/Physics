'''
from matplotlib import pyplot as plt
import csv
'''
import math
import random
class Coord:
    def _init_(self,x=0,y=0):
        self.x = x
        self.y = y
    def x(self):
        return self.x
    def y(self):
        return self.y
    def randmove(self):
        a = 2*math.pi*random.random()
        self.x = self.x+math.cos(a)
        self.y = self.y+math.sin(a)
        return (self)
    def _str_(self):
        return (f"({self.x},{self.y})")
    def dist(self):
        return (self.x*self.x + self.y*self.y)**0.5
def trial(num):
    b = Coord(0,0)
    for i in range(0,num):
        b = b.randmove()
    return (b)

with open('text.txt','a') as a:
    lis = []
    for i in range(1,10000):
        b = trial(1000)
        a.write(f"{b.x},{b.y}\n")
'''
x = []
y = []
i = 0
with open('text.txt','r') as a:
    b = csv.reader(a)
    for line in b:
        i+= 1
        if i <= 10000:
            x.append((float(line[0])))
            y.append((float(line[1])))
        else:
            break

plt.style.use("fivethirtyeight")
plt.scatter(x,y,marker = 'o',alpha = 0.75,c = '#111111',s = 3)
plt.xticks(range(-100,101,25),range(-100,101,25))
plt.yticks(range(-100,101,25),range(-100,101,25))
plt.title("Drunk man")
plt.xlabel("X")
plt.ylabel("Y")
plt.tight_layout()
plt.show()
```
