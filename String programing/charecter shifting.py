n = input ("Please enter the word")
print (n)
for x in range (len(n)):
    print (x,end="")
print()
i = int(input("Please enter the position of the letter"))
p = input("Please enter l for left and r for right")
s = int(input("Please enter how want places you want to shift"))
w= ""
for x in range (len(n)):
    if (n[x] == n[i]):
        w = w
    else:
        w = w+n[x]
print (w)
l = len(n)-1
r = i
if (p == "r"):
    for y in range (s):
        if (r == l):
            r = 0
        else:
            r = r+1
elif (p == "l"):
    for y in range (s):
        if (r == 0):
            r = l
        else:
            r = r-1
print (r)
a = [0]*len(n)
o = ""
if (p == "l"):
    for q in range (len(w)):
        if (q == r):
            a[q] = n[i]
        else:
            a[q] = w[q]
print (a)