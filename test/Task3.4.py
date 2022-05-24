import numpy as np
import math

def find_LU(Matrix):
    n = Matrix.shape[1]
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            Matrix[k, i] = Matrix[k, i] / Matrix[k, k]
        for j in range(k + 1, n):
            for i in range(k + 1, n):
                Matrix[i, j] -= Matrix[i, k] * Matrix[k, j]
    return Matrix

def solve_LU(Matrix, b):
    y = np.matrix(np.zeros([Matrix.shape[0], 1]))
    for i in range(y.shape[0]):
        y[i, 0] = (b[i, 0] - Matrix[i, :i] * y[:i]) / Matrix[i, i]
    x = np.matrix(np.zeros([Matrix.shape[0], 1]))
    for i in range(1, x.shape[0] + 1):
        x[-i, 0] = (y[-i] - Matrix[-i, -i:] * x[-i:, 0])
    return x


A = np.array([[0.9 * math.cos(math.radians(30)), math.sin(math.radians(30)), -1],
              [1.1 * math.cos(math.radians(45)), math.sin(math.radians(45)), -1],
              [1.9 * math.cos(math.radians(60)), math.sin(math.radians(60)), -1]])

print("Matrix A:")
print(A)
print("--------------------------------------")

b = np.array([[math.pow(0.9, 2)], [math.pow(1.1, 2)], [math.pow(1.9, 2)]])
print("Vector b:")
print(b)

solve = solve_LU(find_LU(A), b)
print("----------------------------")
print('Solve:')
print(solve)

a1 = solve[0,0] / 2
a3 = solve[1,0] / (2 * a1)
a2 = math.pow((math.pow(a1, 2) + math.pow(a3, 2) - solve[2,0]), 0.5)
print("----------------------------")
print('a1 =',a1)
print('a2 =',a2)
print('a3 =',a3)


