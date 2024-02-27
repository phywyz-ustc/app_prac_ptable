import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
num_particles = 90
num_steps = 16000
dt = 0.002
d=0.8
box_length = 15.0


history=np.load('C:/Users/WYZ/Desktop/计算物理大作业/16000/historyunderf2950.npy')
#historyo=np.load('C:/Users/WYZ/Desktop/historyo.npy')
# 绘制动画
positions=history[0]
def rou(positions, box_length, cut):
    rou = np.zeros(num_particles)
    s=np.pi*cut*cut
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i != j:
                rij = positions[j] - positions[i]
                rij = rij - np.round(rij / box_length) * box_length  # PBC
                r = np.linalg.norm(rij)
                if r < cut:
                    rou[i]+=1
    return (rou+1)/s
rou1=rou(positions,box_length,4)
plt.figure(1)
plt.hist(rou1,bins=100,range=(0,1))

positions=history[-1]
rou2=rou(positions,box_length,4)
plt.figure(2)
plt.hist(rou2,bins=100,range=(0,1))


plt.figure(3)
plt.plot(history[-1][:,0], history[-1][:,1],'bo', ms=20)

fig, ax = plt.subplots()
ax.set_xlim(0, box_length)
ax.set_ylim(0, box_length)
particles, = ax.plot([], [], 'bo', ms=20)



def update(frame):
   particles.set_data(history[frame][:,0], history[frame][:,1])
   return particles,

ani = FuncAnimation(fig, update, frames=num_steps, interval=50)
plt.show()
