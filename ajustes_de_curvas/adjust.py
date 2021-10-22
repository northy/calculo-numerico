import os, sys, inspect
import numpy as np

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
import sistemas_lineares.linsys as linsys

def normal_eq_mats(P:np.ndarray, d:int) :
    A = np.array([[x**i for i in range(d)] for x,_ in P])
    B = np.array([[y] for _,y in P])
    if B.shape[0]!=A.shape[0] : B = B.T

    return A, B

def solve_normal_eq(A:np.ndarray, B:np.ndarray) :
    assert A.shape[0]==B.shape[0]

    C = A.T.dot(A)
    D = A.T.dot(B)

    return linsys.invMatSolve(C,D)

pol_eq = lambda x, coef : sum(coef[i]*(x**i) for i in range(len(coef)))

def r2(P:np.ndarray, coef:np.ndarray) :
    f = lambda x : pol_eq(x,coef)
    avg = sum(y for _,y in P)/len(P)
    return 1-sum((y-f(x))**2 for x,y in P)/sum((y-avg)**2 for _,y in P)
