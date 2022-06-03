import numpy as np
import math
import copy

def simple_itheration(a, b, n, g):
    x = np.zeros(len(a[0]))
    array = []
    for i in range(len(a[0])):
        array.append(1. - a[i][i])
        a[i][i] = 0.
    sum = 0
    for j in range(len(a[0])):
        for k in range(len(a[0])):
            sum += a[j][k]**2
    if sum < 1:
        print("Converge.") 
    else:
        print("Don't converge.")
    for i in range(len(a[0])):
        for j in range(len(a[0])):
            if i != j:
                a[i][j] /= array[i]
        b[i]/=array[i]
    for i in range(n):
        x_new = (np.dot(a, x) + b)
        lc = []
        for j in range(len(x)):
            lc.append(abs(x[j] - x_new[j]))
        if max(lc) < g:
            print('Count of itherations:',i+1)
            return x_new
        x = x_new
    return x

a = [[0.21, 0.12, -0.34, -0.16], 
     [0.34, -0.08, 0.17, -0.18], 
     [0.16, 0.34, 0.15, -0.31],
     [0.12, -0.26, -0.08, 0.25]]

b = [0.64, -1.42, 0.42, -0.83]
g = 0.001

print("Solution:", simple_itheration(a, b, 100, g))
