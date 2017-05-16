import numpy as np
import matplotlib.pyplot as plt
from math import *

from curve_length import *
from interpolation import *

size=500 #number of point to compute
pmap=np.zeros([size,size]) #
lstep=0.05

fex=[]
fin=[]
for i in range(size) :
    fex.append(extrados(i/size))
    fin.append(intrados(i/size))
hmax=max(fex)
hmin=min(fin)

def exdos(rx) :
    if rx<0 :
        rx=0
    if rx>=size :
        rx=size-1
    return fex[rx]

def indos(rx) :
    if rx<0 :
        rx=0
    if rx>=size :
        rx=size-1
    return fin[rx]

nl=int(1/lstep)

prex=[0 for i in range(nl+1)]
prin=[0 for i in range(nl+1)]

for i in range(nl+1) :
    lmbda = i*lstep
    prex[i] = length_curve(
        lambda x: (lmbda*3*hmax) + (1-lmbda)*exdos(int(round(x*size))),
        1/size, 1-(1/size), step=1/size)
    prin[i] = length_curve(
        lambda x: (lmbda*3*hmin) + (1-lmbda)*indos(int(round(x*size))),
        1/size, 1-(1/size), step=1/size)


def pressex(lmbda) :
    return prex[floor(lmbda*nl)]

def pressin(lmbda) :
    return prin[floor(lmbda*nl)]

for ry in range(size) :
    for rx in range(size) :
        y = (size-ry - (hmin/(hmin-hmax))*size) * (3*(hmax-hmin)/size)
        x = rx/size
        if y >= exdos(rx) :
            pmap[ry][rx] = pressex((y - exdos(rx)) / (3*hmax + exdos(rx)))
        elif y <= indos(rx) :
            pmap[ry][rx] = pressin((y - indos(rx)) / (3*hmin + indos(rx)))
        else :
            pmap[ry][rx] = pmap[0][0]

                    
plt.imshow(pmap,cmap="hot")
plt.show()

