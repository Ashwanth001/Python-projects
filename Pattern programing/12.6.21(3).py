n = input ("Please enter the input")
c = len(n)
cc = c
for x in range (c):
    for y in range (c):
        print (n[y],end="")
    c = c-1
    print ()
