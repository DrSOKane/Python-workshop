import numpy as np
import matplotlib.pyplot as plt



nt=100
nx=100
dx=0.01
dt=1
alpha=1.172e-5
ta=50; tb=50;


X=np.arange(0,0.5,dx)
Temp=np.zeros(int(0.5/dx))
Temp2=np.zeros(int(0.5/dx))

Temp2 = Temp

print(Temp.shape[0],Temp2.shape[0])

Temp[:]=10
Temp[0]=50
Temp[-1]=50	
print(Temp)

for p in range(3600):
	for i in range(1,Temp.shape[0]-1):
		Temp2[i]= alpha*dt/dx**2 * (Temp[i+1]+Temp[i-1])+(1-(2*alpha*dt/dx**2))*Temp[i]
	Temp[:] = Temp2

plt.plot(X,Temp)
plt.show()