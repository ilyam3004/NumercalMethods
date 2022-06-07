from scipy import interpolate
from scipy.interpolate import lagrange
from numpy.polynomial.polynomial import Polynomial
import numpy as np

x = np.array([0.284, 0.883, 1.384, 1.856, 2.644])
y = np.array([-3.856, -3.953, -5.112, -7.632, -8.011])
polynom = lagrange(x, y)
print("Polynom of lagrange:", Polynomial(polynom.coef[::-1])(x[0]+x[1]))
f = interpolate.interp1d(x, y, axis=0, fill_value="extrapolate")
f1 = interpolate.interp1d(x, y, kind='cubic', fill_value="extrapolate")
print("Linear spline(x1+x2):", f(x[0]+x[1]))
print("Linear square spline(x1+x2):", f1(x[0]+x[1]))