import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


n = 100000000
r = 1.0
a,b = (0.0,0.0)
xmin, xmax = a-r, a+r
ymin, ymax = b-r, b+r

x = np.random.uniform(xmin,xmax,n)
y = np.random.uniform(ymin,ymax,n)

fig = plt.figure(figsize=(6,6))
axes = fig.add_subplot(1,1,1)#添加子图
#画子图
plt.plot(x,y,'ko',markersize = 1) #plot绘图 markersize表示点的大小；‘ro’r表示red，o表示圆圈
plt.axis('equal')

d = np.sqrt((x-a)**2 + (y-a)**2)
#res 得到圆中的点数
res = sum(np.where(d<r,1,0)) #numpy.where(conditon,x,y) 满足条件输出x，不满足输出y

pi = res/n*4
print('pi=',pi)
#计算pi的近似值，蒙特卡洛模拟方法，用统计值去近似真实值

#绘制圆形子图
circle = Circle(xy = (a,b), radius = r,alpha = 0.5, color = 'gray')
axes.add_patch(circle)#添加圆形子图
plt.grid(True,linestyle = '--',linewidth = '0.8')
plt.show()
