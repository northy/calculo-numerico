import numpy as np

def solve(A,b,e,lim) :
    F = []
    d = []

    for i in range(len(A)) :
        F.append(A[i]/A[i][i])
        d.append(b[i]/A[i][i])

    F = np.array(F)
    d = np.array(d).reshape(-1,1)

    x = np.zeros(d.shape)
    n = 0

    while np.linalg.norm(A.dot(x)-b)>=e and n<lim :
        x = (np.identity(F.shape[0])-F).dot(x) + d
        n+=1
    
    return x, n
