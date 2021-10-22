def findRoot(f,a,b,e) :
    x = (a+b)/2
    n = 0
    while abs(f(x))>e :
        fx = f(x)
        if fx*f(a)<0 : b = x
        elif fx*f(b)<0 : a = x
        else :
            raise Exception("Sem Raiz no intervalo")
        x = (a+b)/2
        n+=1
    return x, n

def printRoot(f,a,b,e) :
    try :
        print(f"Raiz no intervalo [{a},{b}]: {findRoot(f,a,b,e)[0]}")
    except :
        print(f"Raiz no intervalo [{a},{b}] não existe!")        
