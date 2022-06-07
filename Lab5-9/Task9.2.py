import math
import matplotlib.pyplot as plt
import numpy as np

f = lambda x, y: math.sqrt(4 * (x ** 2) + 1) - 3 * y ** 2
h = 0.2
x = np.arange(2.6, 4.6 + h, h)
y0 = 1.8
y = np.zeros(len(x))
y[0] = y0

#n=3
for i in range (0, len(x) - 1):
    k1 = f(x[i], y[i])
    k2 = f(x[i] + h/2., y[i]+h/2.*k1)
    k3 = f(x[i] + h/2., y[i]+h/2.*k2)
    y[i + 1] = y[i] + h/6.*(k1+2*k2+2*k3)
print("------------- Method Runge-Kuta --------------")
print("For n = 3")
print("x:", x)
print("y:", y)
hd = h

x2 = np.arange(2.6, 4.6 + hd, hd)
y2 = np.zeros(len(x2))
y2[0] = y0

#n=4
for i in range (0, len(x2) - 1):
    k1 = f(x2[i], y2[i])
    k2 = f(x2[i] + hd/2., y2[i]+h/2.*k1)
    k3 = f(x2[i] + hd/2., y2[i]+h/2.*k2)
    k4 = f(x2[i] + hd, y2[i]+h*k3)
    y2[i + 1] = y2[i] + hd/6.*(k1+2*k2+2*k3+k4)

print("-----------------------------------")
print("For n = 4")
print("x:", x2)
print("y:", y2)

plt.figure(figsize=(10, 5))
plt.plot(x, y, 'bo--', label='n = 3')
plt.plot(x2, y2, 'go--', label='n = 4')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend(loc='lower right')
plt.show()

