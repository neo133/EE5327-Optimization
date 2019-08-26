import numpy as np
import matplotlib.pyplot as plt


#Plotting log(x)
x = np.linspace(0.5,8,50)#points on the x axis
#f=np.log(x)#Objective function
f=x*x
plt.plot(x,f,color=(1,0,1))
plt.grid()
plt.xlabel('$x$')
plt.ylabel('$y=x^2$')


#Plot commands
#Plotting line segments with x>0 and y=logx 
#color used to color each line with a different color
plt.plot([1,4],[1,16],color=(1,0,0),marker='o',label="($1$,$1$)-($4$,$16$)")
plt.plot([2,6],[4,36],color=(0,1,0),marker='o',label="($2$,$4$)-($6$,$36$)")
plt.plot([3,5],[9,25],color=(0,0,1),marker='o',label="($3$,$9$)-($5$,$25$)")
plt.legend(loc=2)
plt.show()#Reveals the plot










