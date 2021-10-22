import numpy as np
from functools import reduce

def solve(x,xi,yi) :
    divoperator = lambda n,i : yi[i] if n==0 else (divoperator(n-1,i+1) - divoperator(n-1,i))/(xi[i+n]-xi[i])
    return yi[0]+sum(divoperator(i,0)*reduce(lambda a,b : a*b, [x-xi[j] for j in range(i)], 1) for i in range(1,len(xi)))
