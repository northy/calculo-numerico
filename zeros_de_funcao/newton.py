def newton(f,fp,x) :
    return x-(f(x)/fp(x))

dx = 1e-10
def derivApprox(f,x) :
    return (f(x+dx)-f(x))/dx

def findRoot(f,fp,a,b,e) :
    xm = (a+b)/2
    if fp(xm)*derivApprox(fp,xm)>0 :
        x = b
    else :
        x = a
    x = newton(f,fp,x)
    n = 0
    while abs(f(x)) > e :
        x = newton(f,fp,x)
        n+=1
    
    return x,n

def printRoot(f,fp,a,b,e) :
    try :
        print(f"Raiz no intervalo [{a},{b}]: {findRoot(f,fp,a,b,e)[0]}")
    except :
        print(f"Raiz no intervalo [{a},{b}] não existe!")        
