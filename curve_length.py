
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
