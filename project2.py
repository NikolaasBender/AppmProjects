#PROJECT 2
#NICK BENDER

#https://docs.scipy.org/doc/numpy/reference/routines.linalg.html

import numpy as np
from numpy import matrix
from numpy import linalg
import math
from scipy import *
from scipy import integrate
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from scipy.linalg import eig
import decimal

def printr(B):
	np.set_printoptions(suppress=True)
	print(np.matrix(B))

def plotterS(x, title):
    plt.title(title)
    plt.scatter(x)
    plt.show()

def searchr(x, arr):
	mx = x[0]
	ret = 0
	for y in range(0,len(x)):
		if x[y] > mx:
			mx = x[y]
			ret = y

	return arr[ret]


def bars(wrong, mast, atit, btit, ctit, tit):

	mtx = [[0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0], 
			[0, 0, 0, 0, 0, 0, 0]]

	for x in range(0, 7):
		for y in range(0, 7):
			if mast.item((x,y)) != 0:
				mtx[x][y] = wrong[x][y]
				

	width = 0.2
	a = np.zeros(7)
	c = np.zeros(7)
	b = np.zeros(7)
	a = mtx[0]
	for x in range(0,7):
		b[x] = mtx[x][x]
		c[x] = mtx[x][(x+1)%6]

	offset = 1

	plt.bar(1-width, a[0], width, color='red', label = atit)
	plt.text(1-width, a[0] * offset, float(round(a[0], 2)))

	#LABELING , float(round(c[0], 2))

	plt.bar(1, b[0], width, color='blue', label = btit)
	plt.text(1, b[0] * offset, float(round(b[0], 2)))

	plt.bar(1+width, c[0], width, color='green', label = ctit)
	plt.text(1+width, c[0] * offset, float(round(c[0], 2)))

	for x in range(1, len(a)):
		plt.bar(x-width +1, a[x], width, color='red')
		plt.text(x-width+1, a[x] * offset, float(round(a[x], 2)))

		plt.bar(x +1, b[x], width, color='blue')
		plt.text(x+1, b[x] * offset, float(round(b[x], 2)))

		plt.bar(x+width+1, c[x], width, color='green')
		plt.text(x+width+1, c[x] * offset, float(round(c[x], 2)))


	plt.xlabel('Stage - class')
	plt.ylabel('Effect')
	plt.title(tit)
	plt.legend()
	plt.show()

#SEC 3
F_s = [0,    0,    0,    0,    127,  6,    95]
P_s = [0,    0.74, 0.67, 0.69, 0,    0,    0.83]
G_s = [0.68, 0.05, 0.01, 0.05, 0.82, 0.79, 0]
Popi =[100,  150,  40,   20,   15,   10,   5]

L = np.matrix([[P_s[0], 0, 		0, F_s[3], F_s[4], F_s[5], F_s[6]],
	  		   [G_s[0], P_s[1], 0, 		0, 		0, 		0, 		0],
	  		   [0,  	G_s[1], P_s[2], 0, 		0, 		0, 		0],
			   [0, 		0,    	G_s[2], P_s[3], 0, 		0, 		0],
			   [0, 		0,    	0, 	  	G_s[3], P_s[4], 0,      0],
			   [0, 		0, 	  	0,    	0, 	  	G_s[4], P_s[5], 0],
			   [0, 		0,    	0, 	  	0, 	  	0, 	  	G_s[5], P_s[6]]])

#RIGHT EIGEN VECTORS AND VALUES
eigenvalues, w = linalg.eig(L)

LT = L.transpose()

#LEFT EIGEN VECTORS AND VALUES
eigenvaluesT, v = linalg.eig(LT)

#FINDING LARGEST RIGHT EIGEN VECTOR
wvec = searchr(eigenvalues, w)

#FINDING THE LARGEST LEFT EIGEN VECTOR
vvec = searchr(eigenvaluesT, v)

print(vvec.shape)
print(wvec.shape)


sens = [[0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0], 
		[0, 0, 0, 0, 0, 0, 0]]


print(w[0].size)
print(v.shape)
print(eigenvalues)
#print(sens.item((0,0)))
# print(vvec)

counter = 0
#DOT PRODUCT
wvec2 = np.transpose(wvec)
tot = np.dot(vvec, wvec2)

print(tot)

for x in range(0, 7):
	for y in range(0, 7):
		tmp = np.abs(((w.item(x) * v.item(y))/tot))
		print(tmp)
		sens[x][y] = tmp
		counter += 1
	# np.add(sens, tmp, out=sens, casting="unsafe")
	#print(tmp)
print(counter)

bars(sens, L, 'F_s', 'P_s', 'G_s', 'Sensitivity')

#SENSITIVITY IS DONE

# sensitivity * other 

doot = np.abs(np.dot(L, sens) / maximum)
res = np.asarray(doot)
print(res.shape)

bars(res, L, 'F_s', 'P_s', 'G_s', 'Elasticity')

