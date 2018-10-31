def Bisection(lowerbound,upperbound,tolerance):
    upper=upperbound
    lower=lowerbound
    halfway=(upperbound-lowerbound)/2
    root = 0
    errorflag = 0
    for i in range(1,32):
        fl=function(lower)
        fu=function(upper)
        fh=function(halfway)
        if fl==0:
            root=lower
            break
        elif fh==0:
            root=halfway
            break
        elif fh==0:
            root=upper
            break
        elif fl*fh<0:
            upper = halfway
        elif fh*fu<0:
            lower = halfway
        else
            print("No roots detected. Try setting different bounds.")
            errorflag = 1
            break
        halfway=(upper-lower)/2
        if upper-lower<2*tolerance:
            break
    if root==0 and errorflag==0:
        root=halfway
    return root