n = input ("Please enter the input")
l = len(n)
cl = l-1
for x in range (l+1):
    for y in range (x):
        print (n[cl],end="")
        cl = cl-1
    cl = l-1
    print ()
