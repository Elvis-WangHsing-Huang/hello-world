# matrix calculation practice
# given the following equation,
# 8X1 -3X2 +2X3=20
# 4X1+11X2 -1X3=33
# 6X1 +3X2+12X3=36
# we want to get the solution for X1, X2, X3
# these linear equation can be expressed as A*x = b
# x = Ainvese*b

import numpy as np
from numpy.linalg import inv # linalg => linear algebra

A = np.array([[8., -3., 2.],[4., 11., -1],[6., 3., 12.]])
invA = inv(A)
b = np.array([20., 33., 36.])

x = invA.dot(b) # invA.dot(b) => b is treated as a vector (3X1)
                # not invA*b => b is treaded as a matrix (1X3)
print(x)


# the other way to calculate x by iteration

# X1 =    0*X1+ 3/8*X2 - 2/8*X3 + 20/8
# X2 =-4/11*X1+   0*X2 +1/11*X3 + 33/11
# X3 =-6/12*X1-3/12*X2 +   0*X3 + 36/12
#
# X = B*X + f

B = np.array([[0.,3./8., -2./8. ], [-4./11., 0., 1./11.], [-6./12., -3./12., 0]])
f = np.array([20./8., 33./11., 36./12.])
X = np.array([0., 0., 0.]) # initiallize a zero vector
for i in range(10):
    X = B.dot(X)+f
    print("iteration",i, X)
