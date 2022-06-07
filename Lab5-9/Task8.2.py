import numpy as np
import scipy.integrate as integrate

f = lambda x: (1 + 1.2 * (x ** 2)) / (0.8 + ((x ** 2) + 1.3) ** 0.5)


a = 1.2
b = 2.64
exact = 2.59
ans = []

for N in [1, 2]:
    x = np.linspace(a, b, N + 1)
    an, B = integrate.newton_cotes(N, 1)
    dx = (b - a) / N
    quad = dx * np.sum(an * f(x))
    ans.append(quad)
    error = abs(quad - exact)
    print('{:2d} {:10.9f} {:.5e}'.format(N, quad, error))

print("Runge Rule:", abs(ans[1] - ans[0]) / (2 ** 4 - 1))
