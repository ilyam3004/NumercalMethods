import math

import numpy as np
import scipy.integrate as integrate

f = lambda x: math.sqrt(0.5 * x + 2) / (math.sqrt(2 * (x ** 2) + 1) + 0.8)
f2 = np.vectorize(f)
a = 0.4
b = 1.2
n = 5
t1 = [-0.832498, -0.374513, 0.374513, -0.832498]

x_new = []
real = integrate.fixed_quad(f2, a, b, n=10)[0]
print(real)
for i in range(len(t1)):
    x_new.append((b + a) / 2. + (b - a) / 2. * t1[i])
print("Chebeshow for n=5:", ((b - a) / (n * sum(f2(x_new)))))
print("Absolute error:", abs(real - (b - a) / n * sum(f2(x_new))))
print("Relative error:", abs((real - (b - a) / n * sum(f2(x_new))) / (b - a) / n * sum(f2(x_new))))

n = 6
t1 = [-0.866247, -0.422519, -0.266635, 0.26635, 0.422519, 0.866247]

x_new = []
for i in range(len(t1)):
    x_new.append((b + a) / 2. + (b - a) / 2. * t1[i])

absolute_error = abs(real - (b - a) / n * sum(f2(x_new)))
print("Chebishow for n=6:", ((b - a) / n * sum(f2(x_new))))
print("Absolute error:", absolute_error)
print("Relative error:", abs(absolute_error / (b - a) / n * sum(f2(x_new))))
absolute_error = abs(real - integrate.fixed_quad(f2, a, b, n=5)[0])
print("Gauss for n=5:", integrate.fixed_quad(f2, a, b, n=5)[0])
print("Absolute error:", absolute_error)
print("Relative error:", absolute_error / integrate.fixed_quad(f2, a, b, n=5)[0])
absolute_error = abs(real - integrate.fixed_quad(f2, a, b, n=6)[0])
print("Gauss for n=6:", integrate.fixed_quad(f2, a, b, n=6)[0])
print("Absolute error:", absolute_error)
print("Relative error:", absolute_error/ integrate.fixed_quad(f2, a, b, n=6)[0])