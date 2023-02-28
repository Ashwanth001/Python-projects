def fibo (m,x,y,z,u):
    z = x+y+u
    u = y
    y = x
    x = z
    if (m > 0):
        m = m-1
        print (z,end=" ")
        return fibo(m,x,y,z,u)
    else:
        print(z,end=" ")
l = int(input("Please enter the length of the series"))
if (l < 2):
    print ("The series cannot be developed")
    quit()
else:
    print ("0 1 1 ",end="")
    a = 1
    b = 1
    c = 0
    l = l-3
    t = 0
    fibo(l,a,b,c,t)