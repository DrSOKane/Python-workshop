import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

'''
This program solves a 2D heat conduction problem 


Written by : Nina and Marjan and Simon
31/10/2018
'''

def FDE_interior(interior1,interior2,Temp):
	Temp2=Temp
	for i in interior1 :
		for j in interior2 :
			Temp2[i,j]=alpha * dt /dx **2 * (Temp[i+1,j]+Temp[i-1,j]+Temp[i,j+1]+Temp[i,j-1]) + \
				(1-4 *alpha * dt /dx**2) * Temp[i,j]
	return Temp2

def FDE_edge(edge1_local,edge2_local,Temp):
	Temp2=Temp
	for i in edge1_local:
		for j in edge2_local:
			print(i,j)
			Temp2[i,j]=alpha * dt /dx **2 * (2 * Temp[i-1,j]+Temp[i,j+1]+Temp[i,j-1]+2* T_f *(h * dx /k)) \
				+ (1-4 *alpha * dt /dx**2 -  2* alpha * h * dt /(k * dx) ) * Temp[i,j] 
	return Temp2 

def FDE_corner(c1,c2,Temp):
	Temp2=Temp
	Temp2[c1,c2]=2 * alpha * dt /dx **2 * (Temp[c1-1,c2]+Temp[c1,c2-1]+ 2* T_f *(h * dx /k)) \
		+ (1-4 *alpha * dt /dx**2 -  4* alpha * h * dt /(k * dx) ) * Temp[c1,c2] 	
	return Temp2

nT=200
h=10
alpha=1.4* 10e-7
k=40
rho=1110
T_f=180
dx=0.4/21.0
dt=0.01

n_spacing=21

Temp=np.zeros((21,21))
print(Temp.shape)
#Temp[:,:]=25
Temp[0,:]=180
Temp[:,0]=180
Temp[20,:]=180
Temp[:,20]=180
Temp[1:20,1:20]=25
Temp[10,10]=-15


edge1=np.arange(2,19,dtype=np.int)
edge2=np.ones(18,dtype=np.int)
edge3=np.ones(18,dtype=np.int)*19
print(edge1)
print(edge2)
print(edge3)


interior2=np.arange(2,19,dtype=np.int)
interior1=interior2
print(interior2)

for p in range(nT):
#	corners	
	Temp=FDE_corner(1,1,Temp)
	Temp=FDE_corner(1,19,Temp)
	Temp=FDE_corner(19,1,Temp)
	Temp=FDE_corner(19,19,Temp)
#	edge
	# top
	Temp=FDE_edge(edge2,edge1,Temp)
	#left
	Temp=FDE_edge(edge1,edge2,Temp)
	# right
	Temp=FDE_edge(edge3,edge2,Temp)
	# bottom
	Temp=FDE_edge(edge2,edge3,Temp)
#	interior
	Temp=FDE_interior(interior1,interior2,Temp)


fig=plt.figure()

ax1=fig.add_subplot(111)

ax1.imshow(Temp)


fig.colorbar(ax1.imshow(Temp), orientation='vertical')

plt.show()


#print(Temp)
