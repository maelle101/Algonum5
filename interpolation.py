from load_profile import load_foil

#list of data point (e for extardos and i for intrados)
(dim,ex,ey,ix,iy) = load_foil("boe103.dat")
#print("ex = ",ex)
#print("ey = ",ey)
#print("ix = ",ix)
#print("iy = ",iy)


def spline(x,y):
    print("Je suis dans spline avec len(x) = ",len(x)," et len(y) = ",len(y))
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
    print("spline retourne y2 = " ,y2)
    return y2

def splint(X,Y,x,y2):
    print("je suis dans splint")
    n = len(X)
    kmin = 0
    kmax = n - 1
    print("X[kmin]",X[kmin])
    print("X[kmax]",X[kmax])
    while(kmax - kmin > 1):
        print("kmax =" + str(kmax))
        print("kmin =" + str(kmin))
        k= (kmax+kmin)//2
        print("X[k] = ", X[k])
        print("k = ",k)
        print("x = ",x)
        
        if(X[k] >= x):
            print("dans le if")
            kmax = k
        else :
            print("dans le else")
            kmin = k+1
        print("  ")
    h = (X[kmin] - X[kmax])
    if (h == 0):
        print("erreur in X list")
    a = (X[kmax] - x) /h
    b = (x - X[kmin]) /h
    y = a*Y[kmin] + b*Y[kmax] + ((a**3 - a) * y2[kmax] + (b**3 - b) * y2[kmax])*(h**2)/6.
    return y

print("before spline intra")
y2intra = spline(ix,iy)
print("after spline intra")
y2extra = spline(ex,ey)
print("after spline extra")

def intrados(x):
    print("coucou")
    return splint(ix,iy,x,y2intra)

def extrados(x):
    print("pas coucou")
    return splint(ex,ey,x,y2extra)

print("avant splint intra pour 0,5")
splint(ix,iy,0.5,y2intra)
print("apres splint intra pour 0,5")
