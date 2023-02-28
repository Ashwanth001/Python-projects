u1 = input ("Please enter the upper limit")
l1 = input ("Please enter the lower limit")
u = int(u1)
l = int(l1)
if (l > u):
    print ("Wrong input")
else:
    while (l <=u):
        print (l)
        l = l+1