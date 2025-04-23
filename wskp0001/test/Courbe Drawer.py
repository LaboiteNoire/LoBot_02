"""
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
"""
import numpy as np
import matplotlib.pyplot as plt
import math
x = []
def f(x , n):
    s = 0
    for k in range(n):
        x.append(s)
        s += 0.01
f(x,100)
def fact(n : int):
    if (n == 1) or (n==0):
        return 1
    else:
        return n*fact(n-1)
"""
def proba(x : float , a : float):
    return (math.exp(-a))*((a**x)/math.gamma(x+1))

plt.plot(x, [proba(v,1.5) for v in x])
"""
def func(x : float , n : float , hmax : int):
    return hmax * (math.exp(-math.log(hmax**2/(n*(n+1)))*x))

#plt.plot(x, [func(v,10,100) for v in x])
plt.figure(facecolor="gray")
plt.axes().set_facecolor("black")
plt.plot([0,1],[2,5])
plt.plot([0,1],[8,5])
plt.savefig("test.png")
#plt.show()
