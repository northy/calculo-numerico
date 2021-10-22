import numpy as np
from functools import reduce

def solve(x,xi,yi) :
    return sum(yi[i]*reduce(lambda a,b : a*b, [(x-xi[j])/(xi[i]-xi[j]) for j in range(len(xi)) if j!=i],1) for i in range(len(xi)))
