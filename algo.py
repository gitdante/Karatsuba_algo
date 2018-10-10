

def kalgo(a,b):
    m=max(len(str(a)),len(str(b)))
    if m<=2:
        return a*b
    else:
        c=m//2
        a1=a//(10**c)
        a2=a%(10**c)
        b1=b//(10**c)
        b2=b%(10**c)
        z2=kalgo(a1,b1)
        z0=kalgo(a2,b2)
        z1=kalgo((a1+a2),(b1+b2))-z2-z0
        return z2*10**(2*c)+z1*10**c+z0

x=3141592653589793238462643383279502884197169399375105820974944592
y=2718281828459045235360287471352662497757247093699959574966967627
print(kalgo(x,y))



