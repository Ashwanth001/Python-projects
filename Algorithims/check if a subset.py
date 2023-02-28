s1 = input ("Please enter the first word")
s2 = input ("PLease enter the second word")
c = 0
w = 0
l = len(s2)
for x in s1:
    if (c < l):
        if (x == s2[c]):
            c = c+1
            w = w+1
            if (w == l):
                print (s2,"is a subset of",s1)
            else:
                print (s2,"is not a subset of",s1)
        else:
            w = 0
