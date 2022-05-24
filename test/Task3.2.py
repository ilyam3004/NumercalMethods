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


def find_det(LU):
    n = A.shape[1]
    det = 1
    for k in range(0, n):
        det *= LU[k, k]
    return det


def solve_LU(lu_matrix, b):
    y = np.matrix(np.zeros([lu_matrix.shape[0], 1]))
    for i in range(y.shape[0]):
        y[i, 0] = (b[i, 0] - lu_matrix[i, :i] * y[:i]) / lu_matrix[i, i]
    x = np.matrix(np.zeros([lu_matrix.shape[0], 1]))
    for i in range(1, x.shape[0] + 1):
        x[-i, 0] = (y[-i] - lu_matrix[-i, -i:] * x[-i:, 0])
    return x

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

def get_C(n):
    C = np.zeros([6, 6])
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            C[i, j] = 0.1 * 2.0 * i * j
    return C

def get_a():
    a = np.zeros(36)
    for i in range(0, 6 - 1):
        for j in range(0, 6 - 1):
            a[(i*5)+j] = 1;
    return a

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


A = np.array([[3.51, 0.17, 3.75, -0.28],
              [4.52, 2.11, -0.11, -0.12],
              [-2.11, 3.17, 0.12, -0.15],
              [3.17, 1.81, -3.17, 0.22]])

b = np.array([[0.75], [1.11], [0.21], [0.05]])

LU = find_LU(A)
print('Det:',find_det(LU))
print('Inverse matrix:',inverse(LU))
print('Solve:', solve_LU(LU, b))