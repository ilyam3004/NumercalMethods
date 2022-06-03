import numpy as np

def find_Evklida(A):
    f = 0
    for i in np.arange(A.shape[0]):
        f = f + np.sum(np.power(np.abs(A[i]), 2))
    return np.sqrt(f)


def power(a, x, e):
    tx = x
    itherCount = 1
    while 1:
        x = np.dot(a, x)
        eigenvalue = find_Evklida(x)
        x = x / eigenvalue
        if np.sqrt(sum((tx[i] - x[i]) ** 2 for i in range(len(a)))) <= e:
            print("Relative error:", np.sqrt(sum((tx[i] - x[i]) ** 2 for i in range(len(a)))))
            print("Absoluute error:", abs(eigenvalue - 4.817))
            break;
        tx = x
        itherCount = itherCount + 1
    return eigenvalue, itherCount, x

def rele(a,x,e):
    tl = 0
    itherCount = 1
    while 1:
        x = np.dot(a, x)
        eigenvalue = find_Evklida(x)
        x = x / eigenvalue
        l= x.T @ a @ x
        if abs(tl - l) < e:
            print("Relative error:", abs(tl - l))
            print("Absoluute error:", abs(l - 4.817))
            break
        tl = l
        itherCount = itherCount + 1
    return l, itherCount, x

def inverse_iteration(A, x, nb_iterations):
    n = A.shape[0]
    v = np.random.randn(n)
    v = v/np.linalg.norm(v)
    for i in range(nb_iterations):
        w = np.linalg.inv(A - x * np.eye(n)).dot(v)
        v  = w / np.linalg.norm(w)
        l = v.T.dot(A).dot(v)
    return l, nb_iterations, v

x = np.array([1, 1, 1, 1])
A = np.array([[1., 1.2, 2., 0.5],
     [1.2, 1., 0.4, 1.2],
     [2., 0.4, 2., 1.5],
     [0.5, 1.2, 1.5, 1.]])

print("Power method:")
print(power(A, x, 0.01))
print("----------------------------------------")
print("Power method with rele:")
print(rele(A, x, 0.01))
print("----------------------------------------")
print("Inverse itheration:")
x1 = np.array([0.4, 0.4, 0.4, 0.4])
print(inverse_iteration(A, x1, 3))