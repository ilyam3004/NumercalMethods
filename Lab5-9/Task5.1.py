import numpy as np


def faddeev_leverrier(A):
    A = np.array(A)
    n = A.shape[0]
    assert A.shape[1] == n, 'Array must be square!'
    a = np.array([1.])
    Ak = np.array(A)
    for k in range(1, n + 1):
        ak = -Ak.trace() / k
        a = np.append(a, ak)
        Ak += np.diag(np.repeat(ak, n))
        Ak = np.dot(A, Ak)
    return -a


def newton(x, e, func, dfunc):
    n = 0
    f = 1
    while abs(f) > e:
        f = func(x) / dfunc(x)
        x = x - f
        n += 1
    return x, n


def f(x):
    return p[0] * x ** 3 + p[1] * x ** 2 + p[2] * x + p[3]


def df(x):
    return 3 * p[0] * x ** 2 + 2 * p[1] * x + p[2]


A = [[2.4, 1., 1.4],
     [1., 2.9, 1.4],
     [1.4, 1.4, 3.4]]

p = faddeev_leverrier(A)
print("Polinom:")
print(p)

print("Solution:")
print(newton(1, 0.001, f, df))
print(newton(2, 0.001, f, df))
print(newton(5, 0.001, f, df))

