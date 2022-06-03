import numpy as np
import scipy.linalg

def qr_decomp(A, e=1e-7):
    A_k = A.copy()
    m, n = A.shape
    Q_k = np.eye(n)
    i = 1
    A_t = np.zeros((n, m))
    while True:
        Q, R = np.linalg.qr(A_k)
        Q_k = Q_k @ Q
        A_k = R @ Q
        if np.sqrt(sum((A_k[i][i] - A_t[i][i]) ** 2 for i in range(len(A_t)))) <= e:
            print("Count of itherations:", i)
            break
        else:
            i += 1
            A_t = A_k
    eigenvalues = np.diag(A_k)
    eigenvectors = Q_k
    return eigenvalues, eigenvectors

def lr_decomp(A, e=1e-7):
    A_k = A.copy()
    m, n = A.shape
    i = 1
    A_t = np.zeros((n, m))
    while True:
        P, L, U = scipy.linalg.lu(A_k)
        A_k = U @ L
        if np.sqrt(sum((A_k[i][i] - A_t[i][i]) ** 2 for i in range(len(A_t)))) <= e:
            print(A_k)
            print("Count of itherations:", i)
            break
        else:
            i += 1
            A_t = A_k
    eigenvalues = np.diag(A_k)
    return eigenvalues


def Jacobi_rotation(A, tol=1.0e-9):
    a = A.copy()

    def maxElem(a):
        n = len(a)
        aMax = 0.0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if abs(a[i, j]) >= aMax:
                    aMax = abs(a[i, j])
                    k = i
                    l = j
        return aMax, k, l

    def rotate(a, p, k, l):
        n = len(a)
        aDiff = a[l, l] - a[k, k]

        if abs(a[k, l]) < abs(aDiff) * 1.0e-36:
            t = a[k, l] / aDiff
        else:
            phi = aDiff / (2.0 * a[k, l])
            t = 1.0 / (abs(phi) + np.sqrt(phi ** 2 + 1.0))
            if phi < 0.0:
                t = -t

        c = 1.0 / np.sqrt(t ** 2 + 1.0)
        s = t * c
        tau = s / (1.0 + c)
        temp = a[k, l]
        a[k, l] = 0.0
        a[k, k] = a[k, k] - t * temp
        a[l, l] = a[l, l] + t * temp

        for i in range(k):
            temp = a[i, k]
            a[i, k] = temp - s * (a[i, l] + tau * temp)
            a[i, l] = a[i, l] + s * (temp - tau * a[i, l])

        for i in range(k + 1, l):
            temp = a[k, i]
            a[k, i] = temp - s * (a[i, l] + tau * a[k, i])
            a[i, l] = a[i, l] + s * (temp - tau * a[i, l])

        for i in range(l + 1, n):
            temp = a[k, i]
            a[k, i] = temp - s * (a[l, i] + tau * temp)
            a[l, i] = a[l, i] + s * (temp - tau * a[l, i])

        for i in range(n):
            temp = p[i, k]
            p[i, k] = temp - s * (p[i, l] + tau * p[i, k])
            p[i, l] = p[i, l] + s * (temp - tau * p[i, l])

    n = len(a)
    maxRot = 5 * (n ** 2)
    p = np.identity(n) * 1.0

    for i in range(maxRot):
        aMax, k, l = maxElem(a)

        if aMax < tol:
            print("Count of rotations: " + str(i + 1))
            return np.diagonal(a), p

        rotate(a, p, k, l)

    print('Jacobi method did not converge')


A = np.array([[1., 1.2, 2., 0.5],
              [1.2, 1., 0.4, 1.2],
              [2., 0.4, 2., 1.5],
              [0.5, 1.2, 1.5, 1.]])
print("QR:")
qr = qr_decomp(A)
print(qr[0])
print(qr[1])
print("------------------------------------------")

print("Jacobi rotations:")
jacobi = Jacobi_rotation(A)
print(jacobi[0])
print(jacobi[1])
print("------------------------------------------")

print("LR:")
print(lr_decomp(A))


