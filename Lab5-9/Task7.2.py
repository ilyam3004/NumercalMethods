import math
from numpy import log as ln

a = lambda x: ln(abs(x))
b = lambda x: math.e ** 1.2 + x ** 2
f = lambda x: a(x) ** 2 + b(x) ** 2
x = [5.3, 5.4, 5.5, 5.6, 5.7, 5.8]
y = [f(x[0]), f(x[1]), f(x[2]), f(x[3]), f(x[4]), f(x[5])]
print("x:", x)
print("f(x):", y)



