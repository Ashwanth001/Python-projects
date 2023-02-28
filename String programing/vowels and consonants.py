s = input ("Please enter the string")
s = s+""
c = 0
a = 0
e = 0
i = 0
o = 0
u = 0
for x in s:
    if (x == "a"):
        a = a+1
    elif (x == "e"):
        e = e+1
    elif (x == "i"):
        i = i+1
    elif (x == "o"):
        o = o+1
    elif (x == "u"):
        u = u+1
    else:
        c = c+1
print ("a= ",a)
print ("e= ",e)
print ("i= ",i)
print ("o= ",o)
print ("u= ",u)
print ("consonants= ",c)