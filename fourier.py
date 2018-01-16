import numpy as np
import matplotlib.pyplot as plt
import math

#set 
alpha=1.
l=1.
p=0.8
x = np.arange(0, l, 0.001);
def f(x):
    if x<=p:
        return alpha*x
    else:
        return alpha*p
    
    
def constant (n):
    num=8*alpha*l
    dem=((2*n+1)**2)*((math.pi)**2)
    coeff=num/dem
    num1=(2*n+1)*p*math.pi
    dem1=2*l
    trig=math.sin(num1/dem1)
    return coeff*trig
#print( constant(1))
def fourier(x,n):
    a_n=constant(n) #n=1
    trig=math.sin(((2*n+1)*x*math.pi)/(2*l))
    #print("trig is "+str(trig))
    return a_n*math.sin(((2*n+1)*x*math.pi)/(2*l))


def fourier_series(x):
    accum=0
    for n in range(10):
        accum+=fourier(x,n)
    return accum
    
    
y=plt.plot(x, list(map(f, x)))
z=plt.plot(x,list(map(fourier_series, x)))

plt.show(y)
plt.show(z)
