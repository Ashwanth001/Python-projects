a = 1
b = 0
c = 0
print (1,end=" ")
for x in range (4):
    c = a+b
    b = a
    a = c
    print (c,end=" ")

