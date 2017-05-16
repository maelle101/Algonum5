from load_profile import load_foil

#list of data point (e for extardos and i for intrados)
(dim,ex,ey,ix,iy) = load_foil("boe103.dat")


def spline(x,y):
    n = len(x)
    y2 = [0]
    u = [0]
    for i in range(1,n-1):
        sig = (x[i]-x[i-1])/(x[i+1]-x[i-1])
        p = sig * y2[i-1] + 2.
        y2.append((sig - 1.) / p)
        u.append((6. * ((y[i+1]-y[i])/(x[i+1]-x[i]) - (y[i]-y[i-1])/(x[i]-x[i-1])) / (x[i+1]-x[i-1]) - sig*u[i-1])/p)
    y2.append(1)
    for i in range(n-2,0,-1):
        y2[i]=y2[i] * y2[i+1] + u[i]
    return y2

def splint(X,Y,x,y2):
    n = len(X)
    kmin = 0
    kmax = n - 1
    while(kmax - kmin > 1):
        k= (kmax+kmin)//2
        if(X[k] > x):
            kmax = k
        else :
            kmin = k
    h = (X[kmin] - X[kmax])
    if (h == 0):
        print("erreur in X list")
    a = (X[kmax] - x) /h
    b = (x - X[kmin]) /h
    y = a*Y[kmin] + b*Y[kmax] + ((a**3 - a) * y2[kmax] + (b**3 - b) * y2[kmax])*(h**2)/6.
    return y


y2intra = spline(ix,iy)
y2extra = spline(ex,ey)

def intrados(x):
    return splint(ix,iy,x,y2intra)

def extrados(x):
    return splint(ex,ey,x,y2extra)

