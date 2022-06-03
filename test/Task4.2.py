import numpy as np
import math
import copy

def G_S(a, b, x, g):   
    x = x.astype(float)    
    m, n = a.shape
    times = 0                    
    while True:
        for i in range(n):
            s1 = 0
            tempx = x.copy()        
            for j in range(n):
                if i != j:
                    s1 += x[j] * a[i][j]
            x[i] = (b[i] - s1) / a[i][i]
            times += 1                                   
        gap = max(abs(x - tempx))              
        if gap < g:                          
            break
        elif times > 10000:          
            break
            print("10000 iterations don't converge")
    print("Gaus-Zeidel method:")
    print("Iterations count:",times)
    print("Solution:",x)

def isNeedToComplete(x_old, x_new):
    eps = 0.001
    sum_up = 0
    sum_low = 0
    for k in range(0, len(x_old)):
        sum_up += ( x_new[k] - x_old[k] ) ** 2
        sum_low += ( x_new[k] ) ** 2
        
    return math.sqrt( sum_up / sum_low ) < eps
 

def Jacobi(a, b):
    count = len(b) 
    x = [1 for k in range(0, count) ] 
    times = 0  
    MAX_ITER = 100    
    while( times < MAX_ITER ):
        x_prev = copy.deepcopy(x)
        for k in range(0, count):
            S = 0
            for j in range(0, count):
                if( j != k ): S = S + a[k][j] * x[j] 
            x[k] = b[k]/a[k][k] - S / a[k][k]
        if isNeedToComplete(x_prev, x) : 
            break
        times += 1
    print("------ Jacobi method ------")
    print("Iterations count:",times)
    print("Solution:",x) 


a = np.array([[2.591, 0.512, 0.128, 0.195], 
                [0.203, 3.469, 0.572, 0.162], 
                [0.256, 0.273, 2.994, 0.501],
                [0.381, 0.219, 0.176, 5.903]])
b = np.array([0.159, 0.380, 0.134, 0.864])
x = np.array([0, 0, 0, 0])
g = 1e-3                                            
G_S(a.copy(), b.copy(), x.copy(), g)

Jacobi(a, b)
