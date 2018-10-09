import math
import sys

sys.setrecursionlimit(10000)

def kalgo(a,b):
    m=len(str(a))
    if m<=2:
        return a*b
    else:
        a1=math.floor(a/(10**int(m/2)))
        a2=a%(10**int(m/2))
        b1=math.floor(b/(10**int(m/2)))
        b2=b%(10**int(m/2))
        z2=kalgo(a1,b1)
        z0=kalgo(a2,b2)
        z1=kalgo((a1+a2),(b1+b2))-z2-z0
        print(a1,a2,b1,b2,z2,z1,z0)
        return z2*10**m+z1*10**int(m/2)+z0


print(kalgo(12345678,87654321))
print(12345678*87654321)


