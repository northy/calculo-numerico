import numpy as np
from functools import reduce

def solve(x,xi,yi) :
    h = xi[1]-xi[0]
    z = lambda x : (x - xi[0])/h
    linoperator = lambda n,i : yi[i] if n==0 else linoperator(n-1,i+1) - linoperator(n-1,i)
    return yi[0]+sum((linoperator(i,0)/np.math.factorial(i))*reduce(lambda a,b : a*b, [z(x)-j for j in range(i)], 1) for i in range(1,len(xi)))
