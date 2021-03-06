from cvxopt import matrix,solvers

A = matrix([
[1.0,1.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,1.0,1.0,1.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,1.0,1.0,1.0],
[-1.0,0.0,0.0,-1.0,0.0,0.0,-1.0,0.0,0.0],
[0.0,-1.0,0.0,0.0,-1.0,0.0,0.0,-1.0,0.0],
[0.0,0.0,-1.0,0.0,0.0,-1.0,0.0,0.0,-1.0],
[-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0,0.0],
[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,-1.0]])

b = matrix([40.0,60.0,10.0,-40.0,-50.0,-20.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0])

c = matrix([2.0,1.0,2.0,9.0,4.0,7.0,1.0,2.0,9.0])

sol = solvers.sdp(c, A.T, b)

print(sol['x'])


