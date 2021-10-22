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

    U = np.triu(F,1) # Upper Triangle
    L = np.tril(F,-1) # Lower Triangle
    D = F-U-L # Main Diagonal
    LDI = np.linalg.inv(L + D)

    while np.linalg.norm(A.dot(x)-b)>=e and n<lim :
        x = LDI.dot(d) - LDI.dot(U).dot(x)
        n+=1
    
    return x, n
