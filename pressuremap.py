import numpy as np
import matplotlib.pyplot as plt
from math import *

from curve_length import *

size=1000
pmap=np.zeros([size,size])
lstep=0.05


from random import randrange

def intrados(x):
    return x*(x-1)*0.5

def extrados(x):
    return x*(1-x)*0.7


fex=[]
fin=[]
for i in range(size) :
    fex.append(extrados(i/size))
    fin.append(intrados(i/size))
hmax=max(fex)
hmin=min(fin)

def exdos(x) :
    return extrados(x)
    #return fex[floor(x*size)]

def indos(x) :
    return intrados(x)
    #return fin[floor(x*size)]

#def pratio(lmbda, ft) :

nl=int(1/lstep)

prex=[0 for i in range(nl+1)]
prin=[0 for i in range(nl+1)]

for i in range(nl+1) :
    lmbda = i*lstep
    prex[i] = length_curve(
        lambda x: (lmbda*3*hmax) + (1-lmbda)*exdos(x),
        1/size, 1-(1/size), step=1/size)
    prin[i] = length_curve(
        lambda x: (lmbda*3*hmin) + (1-lmbda)*indos(x),
        1/size, 1-(1/size), step=1/size)


def pressex(lmbda) :
    return prex[floor(lmbda*nl)]

def pressin(lmbda) :
    return prin[floor(lmbda*nl)]

for ry in range(size) :
    for rx in range(size) :
        y = (size-ry - (hmin/(hmin-hmax))*size) * (3*(hmax-hmin)/size)
        x = rx/size
        if y >= exdos(x) :
            pmap[ry][rx] = pressex((y - exdos(x)) / (3*hmax + exdos(x)))
        elif y <= indos(x) :
            pmap[ry][rx] = pressin((y - indos(x)) / (3*hmin + indos(x)))
        else :
            pmap[ry][rx] = pmap[0][0]

                    
plt.imshow(pmap,cmap="hot")#,interpolation="nearest")
plt.show()

#if __name__ == "__main__" :
    