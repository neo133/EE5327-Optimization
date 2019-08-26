import numpy as np
import matplotlib.pyplot as plt



x1 = np.linspace(-3,3,2000)
x2 = (2-2*x1)
plt.plot(x1,x2,label='$f(x)=2x_1 + x_2 >= 2$')

plt.fill_between(x1,x2,8,x1<=0.6,color = 'grey')

x1 = np.linspace(-3,3,2000)
x2 = 1.33*x1

plt.plot(x1,x2,label='$g1(x)=0.8x_1 - 0.6x_2 <= 0$')

plt.fill_between(x1,x2,8,x1>=0.6,color = 'grey')
#x1 = np.linspace(0,3,2000)
#x2 = 1 - x1
#plt.fill_between(x1,x2,4, x2>0 ,color = 'grey')
#plt.fill((1,3,3,1,1),(0,0,4,4,0),color = 'grey')


plt.plot(0.6,0.8,'o')
plt.annotate('%.2f)' %0.8, xy=(0.6,0.8), xytext=(30,0), textcoords='offset points')
plt.annotate('(%.2f,' %0.6, xy=(0.6,0.8))
plt.plot((0,0.6),(0,0.8),color ='green',label='norm is min. for (0.6,0.8) ')
#plt.plot((0,0),(0,4),label='$g3(x)=x_2 >= 0$')

plt.grid()
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.legend(loc = 'best')
plt.savefig('4.9.pdf')
