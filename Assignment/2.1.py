import numpy as np
import scipy 
import matplotlib.pyplot as plt

#c=[1,2,3,4,5,6]#change c value here


def sq(x,c):
	return x**3 - 3*x*c

#Plotting the function
x = np.linspace(-5,5,50)#points on the x axis
c=[1,2,3]#change c value here

for i in c:
    
    vec_sq = scipy.vectorize(sq)
    f=vec_sq(x,i)#Objective function
    plt.plot(x,f,color=(1,0,1))
    plt.grid()
    plt.xlabel('$x$')
    plt.ylabel('$x^3 -3xc$')

#Convexity/Concavity
    a = -4
    b = 4
    lamda = 0.3

    
    f_a = sq(a,i)
    f_b = sq(b,i)


#Plot commands
    plt.plot([a,a],[0,f_a],color=(1,0,0),marker='o',)
    plt.plot([b,b],[0,f_b],color=(0,1,0),marker='o',)
    plt.plot([a,b],[f_a,f_b],color=(0,1,1))
   # plt.legend()
    plt.show()#Reveals the plot








