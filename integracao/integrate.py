import numpy as np

integral = lambda constant,y,window : constant*sum(sum(window*y[i:i+len(window)]) for i in range(0,len(y)-len(window)+1,len(window)-1))

def trapezoid(h,y) :
    assert len(y)>=2
    return integral(h/2,y,np.array([1,1]))

def simpsons1(h,y) :
    assert len(y)>=3 and len(y)%2==1
    return integral(h/3,y,np.array([1,4,1]))

def simpsons2(h,y) :
    assert len(y)>=4 and (len(y)-4)%3==0
    return integral((3*h)/8,y,np.array([1,3,3,1]))

def getSlice(f,a,b,h) :
    x = []
    x0 = a
    while x0-b<=1e-6 :
        x.append(x0)
        x0+=h
    return f(np.array(x))

def getSliceX(f,a,b,h) :
    x = []
    x0 = a
    #print(x0)
    while x0-b<=1e-6 :
        x.append(x0)
        x0+=h
        #print(x0, x0-b)
    return np.array(x)
