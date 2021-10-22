def cordas(f,a,b) :
    fa = f(a)
    fb = f(b)
    return (a*fb-b*fa)/(fb-fa)

def findRoot(f,a,b,e) :
    x = cordas(f,a,b)
    n = 0
    while abs(f(x))>e :
        if f(a)*f(x)>0 : a=x
        else :           b=x
        x = cordas(f,a,b)
        n+=1
    return x, n

def printRoot(f,a,b,e) :
    try :
        print(f"Raiz no intervalo [{a},{b}]: {findRoot(f,a,b,e)[0]}")
    except :
        print(f"Raiz no intervalo [{a},{b}] não existe!")        
