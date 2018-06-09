# 1) The P is the majority of the population at any given time. The G is the population that is lagging.
# 2) 

# Ncorr = {'eggs', 'larva', 'pupa', 'adults'}

# l1 = {P_1, 0, 0, F_4}
# l2 = {G_1, P_2, 0, 0}
# l3 = {0, G_2, P_3, 0}
# l4 = {0, 0, G_3, P_4}

# for x in range(0, 4):
# 	for y in range(0, 4):
#     	print l(x+1)[y] Ncorr[y] % (y)
#     print "%d" % (x)

# 3) Sea turtles live to be extremely old, death is the least of their concerns

# 4) 
import numpy as np
from numpy import matrix
from numpy import linalg as lin
import math
from scipy import *
from scipy import integrate
from scipy.integrate import odeint
import matplotlib.pyplot as plt


L = np.matrix[0 0 0 100; 0 0.74 0.05 150; 0 0.67 0.01 40; 0 0.69 0.05 20; 127 0 0.82 15; 6 0 0.79 10; 95 0.83 0 5]
