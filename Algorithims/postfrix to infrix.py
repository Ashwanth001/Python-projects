n = input("Please enter the postfrix equation")
l = len(n)
i = [0]*l
i1 = 0
for x in range (l):
    if (n[x] != "+" and n[x] != "-" and n[x] != "*" and n[x] != "/" and n[x] != "^"):
        i[i1] = n[x]
        i1 = i1+1
    else:
        i[i1-2] = "(",i[i1-2],n[x],i[i1-1],")"
        i1=i1-1
print(i)
