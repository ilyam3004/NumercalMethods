import numpy as np
import matplotlib.pyplot as plt

f = lambda x, y: x - y ** 2
h = 0.12
x = np.arange(0, 1.2 + h, h)
y0 = 1

y = np.zeros(len(x))
y[0] = y0

for i in range(0, len(x) - 1):
    y[i + 1] = y[i] + h*f(x[i], y[i])

exact = np.zeros(len(x))

plt.figure(figsize = (10, 5))
plt.plot(x, y, 'bo--', label='Euler method')
plt.plot(x, exact, 'g', label='Exact')
plt.title('Approximate and Exact Solution \
for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()