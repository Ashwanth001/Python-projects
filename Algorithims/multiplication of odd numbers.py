n = int(input("please enter the limit"))
i = 1
m = 0
for x in range (1,n+1,2):
    for y in range (n):
        m = x*i
        print (x,"*",i,"=",m)
        i = i+1
    i = 1