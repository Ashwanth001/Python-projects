b1 = input ("Enter number")
a1 = input ("Enter second number")
c1 = input ("Enter third number")
b = int(b1)
a = int(a1)
c = int(c1)
if (a>b & a>c):
    print (a,"is greater than",b,"and",c)
elif (b>a & b>c):
    print (b,"is greater than",a,"and",c)
else:
    print (c,"is greater than",a,"and",b)
