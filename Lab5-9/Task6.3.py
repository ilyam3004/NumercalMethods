import numpy as np

def qr_decomp(A, e):
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
            print("Count of itherations:",i,"for",e,"accurancy")
            break
        else:
            i += 1
            A_t = A_k
    eigenvalues = np.diag(A_k)
    eigenvectors = Q_k
    return eigenvalues, eigenvectors

A = np.array([[2.11, 3.01, 4.02, 0.22],
              [0.18, 3.41, 0.15, 1.43],
              [2.14, 0.17, 0.26, 0.18],
              [1.28, 0.42, 0.54, 1.00]])
print("QR:")
qr = qr_decomp(A, 0.01)
print(qr[0])
print(qr[1])
print("------------------------------------------")

print("QR:")
qr = qr_decomp(A, 0.001)
print(qr[0])
print(qr[1])
print("------------------------------------------")