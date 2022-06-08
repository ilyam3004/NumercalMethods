import numpy as np
import math

F = lambda x: math.atan(x)

a = 0
b = 1
n = 1

temp = 0
exact = F(1) - F(0)
print("Real:", exact)

e = 1e-5

while True:
    n = n + 1
    x = np.linspace(a, b, n)
    f = 1 / (1 + x ** 2)
    h = (b - a) / (n - 1)
    triangle = (h / 2) * (f[0] + 2 * sum(f[1:n - 1]) + f[n - 1])
    if abs(triangle - temp) < e:
        break
    temp = triangle
print("------------ Triangle method --------------")
print("Solution:", triangle)
print("Absolute error:", abs(exact - triangle))
print("relative error:", abs((exact - triangle) / triangle))

n = 1
e = 1e-5
temp_simp = 0
while True:
    n = n + 1
    x = np.linspace(a, b, n)
    f = 1 / (1 + x ** 2)
    h = (b - a) / (n - 1)
    simp = (h / 3) * (f[0] + 2 * sum(f[:n - 2:2]) + 4 * sum(f[1:n - 1:2]) + f[n - 1])
    if abs(simp - temp_simp) < e or n > 1000:
        break
    temp_simp = simp

print("------------ Simpson method ---------------")
print("Solution:", simp)
print("Absolute error:", abs(exact - simp))
print("Relative error:", abs((exact - simp) / simp))

e = 1e-6
n = 1
temp_qu = 0
while True:
    n = n + 1
    x = np.linspace(a, b, n)
    f = 1 / (1 + x ** 2)
    h = (b - a) / (n - 1)
    rec = h * sum(f[:n - 1])
    if(abs(rec - temp_qu) < e):
        break
    temp_qu = rec
print("------------ Rectangle method(left) --------------")
print("Solution:", rec)
print("Absolute error:", abs(exact - rec))
print("Relative error:", abs((exact - rec) / rec))




