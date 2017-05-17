from curve_length import *
from math import *

def tests_curve_length():
    #tests the functions above
    print("retative error on computed length of the curve of x->x between 0 and 10 : ")
    value = (np.sqrt(2)*10)
    print("using the midpoint method : ",end='')
    print(abs((length_curve(lambda x:x, 0, 10, integration_method=midpoint) - value)/value))
    print("using the simpson method : ", end='')
    print(abs((length_curve(lambda x:x, 0, 10, integration_method=simpson) - value)/value))
    print("using the trapeze method : ", end='')
    print(abs((length_curve(lambda x:x, 0, 10, integration_method=trapeze) - value)/value))
    
    print("relative error on computed length of the curve of x->x² between 0 and 10 : ")
    value = (np.sqrt(401)*5 + log(np.sqrt(401) + 20)/4)
    print("using the midpoint method : ",end='')
    print(abs((length_curve(lambda x:x*x, 0, 10, integration_method=midpoint) - value)/value))
    print("using the simpson method : ",end='')
    print(abs((length_curve(lambda x:x*x, 0, 10, integration_method=simpson) - value)/value))
    print("using the trapeze method : ",end='')
    print(abs((length_curve(lambda x:x*x, 0, 10, integration_method=trapeze) - value)/value))

    print("relative error on computed length of the curve of x->ch(x) between 0 and 10 : ")
    value = sinh(10)
    print("using the midpoint method : ",end='')
    print(abs((length_curve(lambda x:cosh(x), 0, 10, integration_method=midpoint) - value)/value))
    print("using the simpson method : ",end='')
    print(abs((length_curve(lambda x:cosh(x), 0, 10, integration_method=simpson) - value)/value))
    print("using the trapeze method : ",end='')
    print(abs((length_curve(lambda x:cosh(x), 0, 10, integration_method=trapeze) - value)/value))

def run_tests():
    print("----------TEST CURVES LENGTH----------")
    tests_curve_length()
    print(" ")
    
          
