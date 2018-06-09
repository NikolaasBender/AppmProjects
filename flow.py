import numpy as np
import math
import scipy
from scipy import integrate
from scipy.integrate import odeint
import matplotlib.pyplot as plt
#==================================
# setup stuff
#==================================
#THESE SEEM USEFUL
#x1(0) = x10
#x2(0) = x20

#THESE ARE USEFUL
a = 0.831 # mortality rate of predator
b = 0.0162 # reproduction rate of predator per prey
c = 0.2824 # reproduction rate of prey
d = 0.0211 # mortality rate of predator per prey
x10 = 10 # initial predator population
x20 = 40 # initial prey population

#THESE ARE OUR ODEs
# x1p = -a*x1 + b*x1*x2
# x2p = c*x2 - d*x1*x2

#JACOBIAN MATRIX
#J = [-a+b*x2 b*x1; -d*x2 c-d*x1]



#==================================
# 2.3
#==================================
#1) nullclines and equ poins
    # x1p == 0
        # x1 = 0
        # x2 = a/b
    # x2p == 0
        # x2 = 0
        # x1 = c/d
    # equ pts
        # c/d, a/b
        # 0, 0
        
#2) eigenvalues
    # lam = (-(a-c) +- sqrt((a-c)^2 +4))/2
    # lam = 0, 0.7627, -1.311
    
#3) stability
    # 0.7627 unstable
    # -1.311 stable
    # 0 neutrally stable
    # a/b || c/d == one of these values 

#==================================
# 2.4
#==================================
# 1
# Set the axis limits
sz = 70
x1min = -sz 
x1max = sz 
x2min = -sz 
x2max = sz
#set step size for x1 and x2;
x1step = 1 
x2step = 1
#this creates the axis essentally
x = np.linspace(-sz, sz)
y = np.linspace(-sz, sz)
#generate mesh for plotting
x1, x2 = np.meshgrid(x, y)

# Define the system of equations 
dx1 = -a*x1 + b*x1*x2
dx2 = c*x2 - d*x1*x2

#normalize vectors (to help plotting)
dx11 = dx1/(dx1**2 + dx2**2)**0.5
dx21 = dx2/(dx1**2 + dx2**2)**0.5

# Generate the vector field
plt.figure()
plt.title('Basic Predator Prey Population')
Q = plt.quiver(x1, x2, dx11,dx21, units='width')


#NULLCLINES
#PUT IN A LINE FOR a/b AND c/d
plt.axvline(x = c/d, color = 'r')
plt.axhline(y = a/b, color = 'r')

#LINES FOR x = 0 AND y = 0
plt.axvline(x = 0)
plt.axhline(y = 0)

# The nullclines show us steady state behavior. At specific points
# we have stable solutions or no solutions at all. When there are no prey 
# the predators starve and die. When there are no predators the prey 
# population goes to infinity. 



plt.show()

# 2
# p is an 2d array of predator population and prey population
# t is not going to beused because autonomous ode
def funyon(t, p):
    a = 0.831 # mortality rate of predator
    b = 0.0162 # reproduction rate of predator per prey
    c = 0.2824 # reproduction rate of prey
    d = 0.0211 # mortality rate of predator per prey
    return -a*p[0] + b*p[0]*p[1], c*p[1] - d*p[0]*p[1]

v = scipy.integrate.solve_ivp(funyon, (0, 50), [x10,x20], method='RK45', max_step=0.01)

print('times')
print(v.t)
print('y values')
print(v.y)

plt.figure()
plt.title('Predator Prey Population over time')
plt.plot(v.t, v.y[1], label = 'prey', color = 'r')
plt.plot(v.t, v.y[0], label = 'predators', color = 'b')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.show()

# A
# There is a lag between the prey population and predator population. 
# When the prey population decreases, the predator population will too
# but it will take a little bit of time until that happens. The 
# reverse is true too. When the prey population increases, the
# predator population will too but there is that lag time between 
# the two.

# B
# Period is between 15 and 10 time units, probably months. It 
# looks to be 14 time units just to pick a single number.

# 3
# The population oscilates between lots of population and about
# the original population. This is because when the number of 
# increases the predators have more food so there are more
# predators. Then the abundance of predators kill off the prey
# faster than they can reproduce. The populations are dependant
# on eacother. 

#==================================
# 3.1
#==================================
#THE NEW DEs
#x1l = -a*x1 + b*x1*x2
#x2l = c*x2*(1 - k*x2) - d*x1*x2

# 1
# It is some constant that determines how many animals the
# enviornment can support. k = 1/carying capacity. When k*x2 > 1
# the function will decrease and vice versa.

# 2 
# 0, 0
# no population in the first place
# a/b, c(1-k)/d
# constant values oscilations go towards
# 0, 1/k
# when the prey hits carying capacity and predators die out because
# carying capacity is too low. 

# 3
def funyonL(t, p):
    a = 0.831 # mortality rate of predator
    b = 0.0162 # reproduction rate of predator per prey
    c = 0.2824 # reproduction rate of prey
    d = 0.0211 # mortality rate of predator per prey
    k = 0.001  # 1/carying capacity
    return -a*p[0] + b*p[0]*p[1], c*p[1]*(1 - k*p[1]) - d*p[0]*p[1]

v = scipy.integrate.solve_ivp(funyonL, (0, 200), [x10,x20], method='RK45', max_step=0.01)

# print('times')
# print(v.t)
# print('y values')
# print(v.y)

plt.figure()
plt.title('Logistic Predator Prey Population over time')
plt.plot(v.t, v.y[1], label = 'prey', color = 'r')
plt.plot(v.t, v.y[0], label = 'predators', color = 'b')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.show()

# A
# They are periodic just like before.

# B
# They both approach specific values, so both are asymptotic.

# 4
def funyonL2(t, p):
    a = 0.831 # mortality rate of predator
    b = 0.0162 # reproduction rate of predator per prey
    c = 0.2824 # reproduction rate of prey
    d = 0.0211 # mortality rate of predator per prey
    k = 0.02 # 1/carying capacity
    return -a*p[0] + b*p[0]*p[1], c*p[1]*(1 - k*p[1]) - d*p[0]*p[1]

v = scipy.integrate.solve_ivp(funyonL2, (0, 200), [x10,x20], method='RK45', max_step=0.01)

# print('times')
# print(v.t)
# print('y values')
# print(v.y)

plt.figure()
plt.title('Logistic Predator Prey Population over time with k = 0.02')
plt.plot(v.t, v.y[1], label = 'prey', color = 'r')
plt.plot(v.t, v.y[0], label = 'predators', color = 'b')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.show()

# This is where we see the carying capacity being too low. 
# The prey go to carying capacity and the predators die out.

# 5
# YOU NEED TO DO THIS


#==================================
# 4.1
#==================================

# 1 

def funyonM(t, p):
    a = 0.831 # mortality rate of predator
    b = 0.0162 # reproduction rate of predator per prey
    c = 0.2824 # reproduction rate of prey
    d = 0.0211 # mortality rate of predator per prey
    m = 0.02  # 1/carying capacity
    per = 14 # period from 2
    omeg = 2 * 3.14159 / per # omega value
    return -a*p[0] + b*p[0]*p[1], c*p[1] - d*p[0]*p[1] + m*p[1]*scipy.sin(omeg * t)

v = scipy.integrate.solve_ivp(funyonM, (0, 500), [x10,x20], method='RK45', max_step=0.1)

# print('times')
# print(v.t)
# print('y values')
# print(v.y)

plt.figure()
plt.title('Migration Predator Prey Population over time')
plt.plot(v.t, v.y[1], label = 'prey', color = 'r')
plt.plot(v.t, v.y[0], label = 'predators', color = 'b')
plt.xlabel('Time')
plt.ylabel('Population')
plt.legend()
plt.show()

# 2 
# It looks like oscilations in oscilations. The Model of the 
# predator and prey have the original relationship but it
# is augmented by animals migrating into and out of the region.
# This total population changes the magnitude of the oscilations
# between predator and prey.