import numpy as np
import matplotlib.pyplot as plt

def thermaldiffusion(T0,Ta,Tb,dx,L,dt,tend,alpha):
    x = np.arange(-L/2,L/2,dx)
    Nx = x.shape[0]
    t = np.arange(0,tend,dt)
    Nt = t.shape[0]
    T = T0*np.ones(Nt,Nx)
    T[0,0] = Ta
    T[0,Nx] = Tb
    for i in range(1,Nt):
        T[i,0] = Ta
        T[i,Nx] = Tb
        for j in range(1,Nx-1):
            T[i,j] = T[i-1,j]*(1-2*alpha*dt/(dx*dx))+(T[i-1,j-1]+T[i-1,j+1])*alpha*dt/(dx*dx)
    return T

T = thermaldiffusion(10,50,50,0.01,0.5,1,3600,1172)