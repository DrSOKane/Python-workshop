import numpy as np
import matplotlib.pyplot as plt

def thermaldiffusion(T0,Ta,Tb,dx,L,dt,tend,alpha):
    x = np.arange(-L/2,L/2,dx)
    Nx = x.shape[0]
    t = np.arange(0,tend,dt)
    Nt = t.shape[0]
    T = T0*np.ones([Nt,Nx])
    T[:,0] = Ta
    T[:,Nx-1] = Tb
    for p in range(1,Nt):
        for i in range(1,Nx-1):
            T[p,i] = T[p-1,i]*(1-2*alpha*dt/(dx*dx))+(T[p-1,i-1]+T[p-1,i+1])*alpha*dt/(dx*dx)
    return T

L = 0.5
dx = 0.01
tend = 3600
dt = 1
x = np.arange(-L/2,L/2,dx)
Nx = x.shape[0]
t = np.arange(0,tend,dt)
Nt = t.shape[0]
T = thermaldiffusion(10,50,50,dx,L,dt,tend,1.172e-5)
plt.plot(x,T[Nt-1,:])
plt.show()