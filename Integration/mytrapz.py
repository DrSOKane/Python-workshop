import numpy as np

def integrand(x):
    output=4-(x-2)*(x-2)
    return output

def mytrapz(a,b,dx):
    N=(b-a)/dx
    integral=0
    lower=a
    for i in range(1,int(N)):
        upper=lower+dx
        integral=integral+(integrand(upper)+integrand(lower))*dx/2
        lower=lower+dx
    return integral

exact = 32/3
numerical = mytrapz(0,4,0.2)
fractionalerror = abs(numerical-exact)/exact
print("The fractional error is",fractionalerror)
xarray = np.linspace(0,4,21)
for i in range(1,21):
    yarray = integrand(xarray[i])
withtrapz = np.trapz(yarray,xarray)
discrepancy = abs(numerical-withtrapz)/withtrapz
print("Fractional discrapancy with trapz is",discrepancy)