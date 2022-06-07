import numpy as np
import math

F = lambda x: math.atan(x)

a = 0
b = 1
n = 1

temp_trap = 0
real = F(1) - F(0)
print("Real:", real)

e = 1e-5

while True:
    n = n + 1
    x = np.linspace(a, b, n)
    f = 1 / (1 + x ** 2)
    h = (b - a) / (n - 1)
    I_trap = (h / 2) * (f[0] + 2 * sum(f[1:n - 1]) + f[n - 1])
    if abs(I_trap - temp_trap) < e:
        break
    temp_trap = I_trap
print("Triangle method:", I_trap)
print("Absolute error:", abs(real - I_trap))
print("relative error:", abs((real - I_trap) / I_trap))

n = 1
e = 1e-5
temp_simp = 0
while True:
    n = n + 1
    x = np.linspace(a, b, n)
    f = 1 / (1 + x ** 2)
    h = (b - a) / (n - 1)
    I_simp = (h / 3) * (f[0] + 2 * sum(f[:n - 2:2]) + 4 * sum(f[1:n - 1:2]) + f[n - 1])
    if abs(I_simp - temp_simp) < e or n > 1000:
        break
    temp_simp = I_simp
print("Simpson method:", I_simp)
print("Absolute error:", abs(real - I_simp))
print("Relative error:", abs((real - I_simp) / I_simp))

e = 1e-6
n = 1
temp_qu = 0
while True:
    n = n + 1
    x = np.linspace(a, b, n)
    f = 1 / (1 + x ** 2)
    h = (b - a) / (n - 1)
    I_qu = h * sum(f[:n - 1])
    if(abs(I_qu - temp_qu) < e):
        break
    temp_qu = I_qu
print("Rectangle method:", I_qu)
print("Absolute error:", abs(real - I_qu))
print("Relative error:", abs((real - I_qu) / I_qu))




