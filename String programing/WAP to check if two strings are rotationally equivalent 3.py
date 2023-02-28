n = input ("Please enter the word")
a = input ("Please enter the second word")
b = n+n
c = 0
for x in range (len(n)):
    i = b[x:x+len(n)]
    if (i == a):
        c = 1
    else:
        c = c
if (c == 1):
    print ("The word is rotationally equivalent")
else:
    print ("The word is not rotationally equivalent")