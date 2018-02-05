#TEAM YARRRRRRR (NICK BENDER AND PAUL CHRISTIANSON) PROJECT 1
#https://learn.colorado.edu/d2l/le/content/243218/viewContent/3409779/View
#https://www.youtube.com/watch?v=VV3BnroVjZo

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

#THIS RETURNS dy/dt
def model(y, t):
	
	k = #SOMETHING

	#THIS PROBABLY NEEDS TO BE CHANGED FOR OUR QUESTION
	#WE WILL PROBABLY USE astroPos
	dydt = -k * y

	return dydt

#================================================================
#THIS IS FROM THE WRITEUP SHEAT
#================================================================
def astroPos(x):
	dx = ((2/x) - 1)(1/sqrt(x))
	return dx;

def astroVel(x)
	ddx = (-2/(x ** 2))(x ** -3/2)
	return ddx;

#INITIAL CONDIDTION
y0 = #SOMETHING

#TIME POINTS
start = #STARTPOINT NUMBER EX: 0
end = #ENDPOINT NUMBER EX: 20
tpnum = #THE NUMBER OF STEPS (DEFAULT IS 50)
t = np.linspace(start, end, tpnum)

#SOLVE ODE
y = odeint(model, y0, t)

#================================================================
#THIS PLOTS THE RESULTS
#================================================================
plt.plot(t, y)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.show()


