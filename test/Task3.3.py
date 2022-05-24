import numpy as np

def find_LU(A):
    n = A.shape[1]
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            A[k, i] = A[k, i] / A[k, k]
        for j in range(k + 1, n):
            for i in range(k + 1, n):
                A[i, j] -= A[i, k] * A[k, j]
    return A

def get_L(m):
    L = m.copy()
    for i in range(L.shape[0]):
        L[i, i + 1:] = 0
    return L


def get_U(m):
    U = m.copy()
    for i in range(U.shape[0]):
        U[i, :i] = 0
        U[i, i] = 1
    return U

def inverse(LU):
    l_inv = np.linalg.inv(get_L(LU))
    u_inv = np.linalg.inv(get_U(LU))
    A_inv = np.dot(u_inv, l_inv)
    return A_inv

def func(i, j):
    return 125 / ((4 + 0.1 * N * i * j * 0.25) ** 6);

def evklidNorm(M):
    powSum = 0;
    for i in range(n):
        for j in range(n):
            powSum += pow(abs(M[i, j]), 2)
    return(pow(powSum, 0.5));

def conditionNumber(M):
    return evklidNorm(M) * evklidNorm(inverse(find_LU(M)))

N = 2
n = 3

for i in range(6):
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            A[i, j] = func(i + 1, j + 1)
    print('n = ',n)
    print('Matrix:')
    print(A)
    LU = find_LU(A.copy())
    print('LU Matrix:')
    print(LU)
    INV = inverse(LU.copy())
    print('Inverse matrix:')
    print(INV)
    EVKLID = evklidNorm(A.copy())
    print('Evklid norm:', evklidNorm(A.copy()))
    print('Condition number:',conditionNumber(A.copy()))
    print('-------------------------')
    n = n + 1