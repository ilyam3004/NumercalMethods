import numpy as np
import matplotlib.pyplot as plt

f = lambda x, y: x - y ** 2
h = 0.1
x = np.arange(0, 2 + h, h)
y0 = 1

y = np.zeros(len(x))
y[0] = y0

for i in range(0, len(x) - 1):
    y[i + 1] = y[i] + h*f(x[i], y[i])


print(y)
exact = np.zeros(len(x))
exact[0] = 1
exact[1] = 0.91
exact[2] = 0.839
exact[3] = 0.7902759
exact[4] = 0.73939285
exact[5] = 0.74323389
exact[6] = 0.73947069
exact[7] = 0.74625794
exact[8] = 0.76205037
exact[9] = 0.77649239
exact[10] = 0.80535355
exact[11] = 0.85049411
exact[12] = 0.88985108
exact[13] = 0.92243729
exact[14] = 0.97734823
exact[15] = 1.02377197
exact[16] = 1.07009861
exact[17] = 1.11942681
exact[18] = 1.16656581
exact[19] = 1.21303257
exact[20] = 1.258
print(x)
print(exact)


plt.figure(figsize = (10, 5))
plt.plot(x, y, 'bo--', label='Euler method')
plt.plot(x, exact, 'go--', label='Exact')
plt.title('Approximate and Exact Solution \
for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()