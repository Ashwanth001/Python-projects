n = input ("Please enter the first word")
m = input ("Please enter the second word")
a = [0]*len(n)
c= 0
for x in range (len(n)):
    a[x] = n[x]
b = [0]*len(n)
for x in range (len(m)):
    b[x] = m[x]
for x in range (len(n)):
    for y in range (x):
        print (a)
    if (a == b):
        c = 1
    else:
        c = 0