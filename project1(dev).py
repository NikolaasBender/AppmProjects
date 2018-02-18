
import numpy as np
import math
from scipy import *
from scipy import integrate
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#Euler's Method:
#yn = y1 + h*f(t1, y1)| yn is new y value (n+1); h is timestep; y1 and t1 are initial values

#ananlytical
#we can rearrange, solve, then integrate
#gives us an exact

#numerical 
#we have to use approximations
#gives us an approx

#================================================================================================
#THE DIFF EQ WE WERE GIVEN
#================================================================================================
def astrodx(x):
    ret = ((2./x)-1)*(1./x**.5)
    return ret



#================================================================================================
#ANANLYTICAL FN
#================================================================================================
def ANA(t):
    zoop =  11 - 2 * (t**.5) - (4/(t**.5))
    return zoop



#================================================================================================
#Analytical Solution
#================================================================================================
def Analytical(t, n, step):
    analyticalx = []
    analyticaly = []
    while t < n:
        analyticalx.append(t)
        analyticaly.append(ANA(t))
        t += step

    return analyticalx, analyticaly


#================================================================================================
#THIS SHOULD PLOT THE ACTUAL FUNCTION
#================================================================================================
def plotAct(x, y):
    plt.title('Actual Plot')
    plt.plot(x,y)
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.show()



#================================================================================================
#THIS DOES THE EULER APPROX
#================================================================================================
def newEuler(x0, y0, h, n):
    # print(y0)
    # print(x0)
    xvalues = []
    newy = []
    xvalues.append(x0)
    newy.append(y0)

    while x0 < n:
        
       #print(y0)
        y0 += h*astrodx(x0)
        newy.append(y0)
        xvalues.append(x0)
        #y0 = yn

        x0 = x0 + h

    return xvalues, newy


#================================================================================================
#THIS SHOULD PLOT THE EULER GRAPH
#================================================================================================
def plotEuler(x, y):
    plt.title('Euler Approximation Plot')
    plt.plot(x,y)
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.show()


#================================================================================================
#PLOT BOTH GRAPHS TOGETHER
#================================================================================================
def plotBoth(x, y, c, d):
    plt.title('Approximation and Actual')
    plt.plot(x, y, label = 'Euler approx')
    plt.plot(c, d, label = 'Actual')
    plt.xlabel('Time')
    plt.ylabel('Position')
    plt.legend(loc='upper right')
    plt.show()




#================================================================================================
#================================================================================================
# 4. Using the timestep h = 0.01, plot numerical solutions to the differential equation
# in (1) with various initial conditions x(0) = 5, x(0) = 4, x(0) = 3, and x(0) = 2.
# These solutions should all appear together on one plot. Your plot should include
# 3 a legend. Looking at this plot, does the long-time behavior of this system depend
# on the initial condition? Does this make sense physically?
# 
# 5. We have examined the long-time behavior analytically (using the direction field)
# and numerically (using our Euler solver). Do these results agree? Why or why
# not?
#================================================================================================
#================================================================================================



#================================================================================================
#Q4
#STEP SIZE 0.01
#================================================================================================
#X INITIAL
xi = 1
#Y INITIAL
yi = 5
#STEP SIZE
ste = 0.01
#END PSOITION
end = 200

#DOES THE EULER APPROX
x,y = newEuler(xi, yi, ste, end)
#ERROR CHECKING
plotEuler(x,y)

#DOES THE ACTUAL GRAPH
t,z = Analytical(xi, end, ste)
#MORE ERROR CHECKING REALLY
plotAct(t, z)

plotBoth(x, y, t, z)



#================================================================================================
# Q5
# Yes they agree. The smaller teh step size the more they agree. The only difference between the two 
# is that the analytical solution is shifted vertically by the first term. It is set to 11 to match 
# the Euler Approximation. Even more impressivly even with a realtively large step size the Euler 
# approximation follows the analytical solution pretty well.
#================================================================================================
