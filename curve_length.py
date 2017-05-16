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
