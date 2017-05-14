import numpy as np;
import re; # regexp
import matplotlib.pyplot as ma;

################################################################
# Airfoil : load profile of a wing
#
# Reads a file whose lines contain coordinates of points,
# separated by an empty space.
# Every line not containing a couple of floats is discarded. 
# Returns a couple constitued of the list of points of the
# extrados and the intrados. 
def load_foil(file):
    f = open(file, 'r')
    matchline = lambda line: re.match(r"\s*([\d\.-]+)\s*([\d\.-]+)", line)
    extra  = [];    intra = []
    rextra = False; rintra = False
    for line in f:
        m = matchline(line)
        if (m != None) and not(rextra):
            rextra = True
        if (m != None) and rextra and not(rintra):
            extra.append(m.groups())
        if (m != None) and rextra and rintra:
            intra.append(m.groups())
        if (m == None) and rextra:
            rintra = True

    #print("extra = ", extra)
    ex = np.array(np.reshape(extra, 2*len(extra)), dtype=np.float64)[0::2]
    ey = np.array(np.reshape(extra, 2*len(extra)), dtype=np.float64)[1::2]
    ix = np.array(np.reshape(intra, 2*len(intra)), dtype=np.float64)[0::2]
    iy = np.array(np.reshape(intra, 2*len(intra)), dtype=np.float64)[1::2]
    return(ex,ey,ix,iy)


(ex,ey,ix,iy) = load_foil("datas.dat")
ma.plot(ex,ey)#,ix,iy)
ma.show()
