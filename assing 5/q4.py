
from cvxpy import *
from numpy import matrix

w1 = Variable()
w2 = Variable()
d = Variable()

#Objective
obj = Minimize(w1**2 + w2**2)

#Constraints
constraints = [2*w1 + w2 + d >=1,
               0.8*w1 - 0.6*w2 +d <=-1]

#solution
Problem(obj, constraints).solve()

print('w1 = %.2f'%(w1.value) , 'w2 = %.2f'%(w2.value),'d = %.2f'%(d.value))

print(0.5*((w1.value)*(w1.value)+(w2.value)*(w2.value)))

