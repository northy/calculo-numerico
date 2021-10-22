import numpy as np

def invMatSolve(A,b) :
    return np.linalg.inv(A).dot(b)
