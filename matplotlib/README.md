#matplotlib 
---
##Installation (Ubuntu, Python3)
```
$ sudo apt-get install python3-pip
$ pip3 install -upgrade pip
$ pip3 install matplotlib
$ pip3 install numpy
$ pip3 install scipy
$ sudo apt-get install python3-tk
```

##matplotlib - Inline Graph Display
`%matplotlib inline`

##Import matplotlib plot 
```
import matplotlib.pyplot as plt
```

##Simple plot
### Simple Line PLot
```
import matplotlib.pyplot as pi 
import numpy as np
import math 
x = np.linspace(0, 2*math.pi, 100)
y = np.sin(x)
plt.plot(x, y, label='sin')
plt.show()
```

### Decoration
```
plt.plot(x,y)
plt.title('Sin Graph')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.grid(True)
plt.show()
```
## Bar Graph 
### Bar
```
plt.bar( [1, 3, 5, 7, 9], [5, 2, 7, 8, 2], label=”Example 1”)
plt.bar( [2, 4, 6, 8, 10], [8, 6, 2, 5, 6], label=”Example 2”, color=’g’ )
plt.legend()
plt.xlabel('bar number’)
plt.ylabel('bar height’)
plt.title(‘Bar Graph Sample’)
plt.show()
```

### Histogram
```
plt.hist( occurances, bins, histtype=’bar’, rwidth=0.8 )
```

### Scatter
```
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]
plt.scatter(x, y, label=’scatter’, color=’k’, s=25, marker=”o”) 

```

## Stack Plot 
```
x = [1,2,3,4,5]   # X axis 
y1 = [….]             # first data 
 …
y4 = […]              # 4th data 
plt.plot([],[], color=’m’, label=’Y1’, linewidth=5) 	# fake line for legend
plt.plot([],[], color=’c’,  label=’Y2’, linewidth=5)	# ditto 
… 
plt.stackplot( x, y1, y2, y3, y4, colors=[‘m,’c’,’r’,’k’] )

```

## Pie Chart
```
slices = [7, 2, 2, 13]
activities = [‘sleeping’, ‘eating’, ‘working’, ‘playing’]
cols = [‘c’, ‘m’, ‘r’, ‘b’] 
plt.pie( slices, labels=activites, colors=cols, 
	startangle=90, shadow=True, explode=(0, 0.1, 0, 0), autopct=’%.1f%%’) 
```

---
#APPENDIX: Read CSV File and Plot
```
import numpy as np
x,y = np.loadtxt('test.csv', delimiter=',', unpack=True)
plt.plot(x, y, label='Loaded from File')
```






