import numpy as np
from math import *

def prime(f, x, e) :
    '''Computes the derivative of f at x. e is the precision'''
    return (f(x+e) - f(x-e)) / (2*e)

def trapeze(a, b, f) :
    '''Computes an approximation of the integral between a and b of f'''
    return (f(a) + f(b)) * (b-a) / 2

def midpoint(a, b, f) :
    '''Computes an approximation of the integral between a and b of f'''
    return f((a+b)/2) * (b-a)

def simpson(a, b, f) :
    '''Computes an approximation of the integral between a and b of f'''
    return ((b-a)/6)*(f(a) + 4*f((a+b)/2) + f(b))

def integral(method, a, b, dx, f):
    '''computes an approximation of the integral between a and b of f with step dx using the method method'''
    k = floor((b-a)/dx)
    v = np.linspace(a, b, k)
    result = 0
    for i in range(len(v)-1):
        result += method(v[i], v[i+1], f)
    return result

def length_curve(f, a, b, integration_method=trapeze, precision_prime=0.01, step=0.01):
    '''computes the length of the curve of the function f between a and b using specific integration method'''
    return integral(integration_method,
                    a,
                    b,
                    step,
                    lambda x:np.sqrt(1 + prime(f, x, precision_prime)**2))


def rerror_figure():
    nb = 50
    f2 = lambda x:x**3 
    f2_i = lambda x:(x**4)/4.
    b = range(1,nb+1)
    a = 0
    dx = 0.01

    f2_integ = []
    trapeze_error = []
    for i in range(0,nb):
        f2_integ.append(f2_i(b[i]))
        trapeze_error.append(abs(f2_integ[i] - integral(trapeze, a, b[i], dx, f2))/f2_integ[i])
    plt.plot(b, trapeze_error, label="trapeze")

    midpoint_error = []
    for i in range(0,nb):
        midpoint_error.append(abs(f2_integ[i] - integral(midpoint, a, b[i], dx, f2))/f2_integ[i])
    plt.plot(b, midpoint_error, label="midpoint")

    simpson_error = []
    for i in range(0,nb):
        simpson_error.append(abs(f2_integ[i] - integral(simpson, a, b[i], dx, f2))/f2_integ[i])
    plt.plot(b, simpson_error, label="simpson")
  
    plt.xlabel("x")
    plt.ylabel("rerror")
    plt.legend()
    plt.title("Relative Error of the differents Integration Methods (x->x^3)")

    plt.show()



if __name__ == '__main__':
    rerror_figure()
