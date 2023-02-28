sc = input ("Please enter the typing sentence")
st = input ("Type the sentence")
lsc = len(sc)
c=0
e = 0
cst = ""
for x in range (1,lsc):
    for y in sc:
        if (y == (st[x])):
            c = c+1
        else:
         e = e+1
         cst = (st[x])
         print (cst)
print ("correct= ",c)
print ("incorrect= ",end="")
