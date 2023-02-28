n = input ("Please enter the input ")
l = len(n)
pr = ""
pa = ""
for x in range (l):
    pr = n[x]
    if (pr == pa):
        print (pr)
    pa = pr