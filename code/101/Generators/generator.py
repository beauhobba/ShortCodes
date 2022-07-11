from matplotlib import pyplot as plt
from matplotlib import animation
import math 
  

def MulTwo(n):
    i = 0
    while True:
        n = math.degrees(math.cos(n))
        i += 1
        yield n, i
        
        
        
        
a = MulTwo(1)


fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
x_arr = []
y_arr = []

line, = ax.plot([], [], lw=2)


def init():
    line.set_data([], [])
    return line,

def animate(i):
    
    val, i = next(a)
    print(val)
    x_arr.append(i)
    y_arr.append(val)
    
    line.set_data(x_arr, y_arr)
    ax.set_ylim(-360, 360)
    ax.set_xlim(0, 100)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=200, blit=False)

plt.autoscale(enable=True, axis='y', tight=False)
plt.show()