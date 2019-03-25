import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors
 
#funcio f(x) = x^3-A
def f(x1, x2):
	return np.power(x1, 3) - x2


#funcio f(x) = 3x^2
def fp(x1, x2):
	return 3*np.power(x1, 2)

#metode Newton-Raphson

decimalstep = np.arange(-100, 100, 0.1) #vector para stepear 0.1 la A de -100 a 100
llista_A = [] #valors de A
llista_A3 = [] #valors de A^(1/3)
llista_num=[] 


for i in decimalstep:
    x = 1.0
    ok = 0
    num = 0
    while ok == 0 and num < 2000:
        xnew = x - (f(x,i)/fp(x, i))
        num += 1
        if abs(xnew - x) < 0.00000001:
            ok = 1
        x = xnew
    llista_A.append(i)
    llista_A3.append(x)
    llista_num.append(num)
    


plt.plot(llista_A,llista_A3)
plt.grid(True)
plt.show()
plt.plot(llista_A,llista_num)

plt.grid(True)

plt.show()