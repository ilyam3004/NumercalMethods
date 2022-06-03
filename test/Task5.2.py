import numpy as np

def find_Evklida(A):
    f = 0
    for i in np.arange(A.shape[0]):
        for j in np.arange(A.shape[1]):
            f = f + np.sum(np.power(np.abs(A[i, j]), 2))
    return np.sqrt(f)


A = np.array([[1., 1.2, 2., 0.5],
              [1.2, 1., 0.4, 1.2],
              [2., 0.4, 2., 1.5],
              [0.5, 1.2, 1.5, 1.]])

a = find_Evklida(A)
b = find_Evklida(np.linalg.inv(A.copy()))
print("Evklid number", a)
print("Condition number:", a * b)
print("Limits of eigenvalues:")
print("[-2.7, 5.9]")