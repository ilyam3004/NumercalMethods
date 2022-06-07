import math
import numpy as np
import matplotlib.pyplot as plt

f = lambda x, y: math.cos(x+y) + 0.5 * (x - y)
h = 0.1
x = np.arange(0, 1 + h, h)
y = np.zeros(len(x))
y[0] = 0


for i in range (0, 2):
    k1 = f(x[i], y[i])
    k2 = f(x[i] + h / 2., y[i] + h / 2. * k1)
    k3 = f(x[i] + h, y[i] - h * k1 + 2 * h * k2)
    y[i + 1] = y[i] + h / 6. * (k1 + 4 * k2 + k3)
for i in range(2, len(x) - 1):
    y[i + 1] = y[i] + h / 15. * (23 * f(x[i], y[i]) - 16 * f(x[i], y[i - 1]) + 5 * f(x[i], y[i-2]))


h2 = 0.1
x2 = np.arange(0, 1 + h2, h2)
y2 = np.zeros(len(x2))
y2[0] = 0

#n=3
for i in range (0, len(x2) - 1):
    k1 = f(x2[i], y2[i])
    k2 = f(x2[i] + h2/2., y2[i]+h2/2.*k1)
    k3 = f(x2[i] + h2/2., y2[i]+h2/2.*k2)
    y2[i + 1] = y2[i] + h2/6.*(k1+2*k2+2*k3)

print(x2)
print(y2)

plt.figure(figsize=(10, 5))
plt.plot(x, y, 'bo--', label='n = 3')
plt.plot(x2, y2, 'go--', label='n = 3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid()
plt.legend(loc='lower right')
plt.show()