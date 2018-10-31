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
print("Integral with mytrapz is",numerical)
fractionalerror = abs(numerical-exact)/exact
print("The fractional error is",fractionalerror)
xarray = np.arange(0,4,0.2)
yarray=integrand(xarray)
withtrapz = np.trapz(yarray,xarray)
print("Integral with np.trapz is",withtrapz)
discrepancy = abs(numerical-withtrapz)/withtrapz
print("Fractional discrepancy with trapz is",discrepancy)