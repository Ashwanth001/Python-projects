n = input ("Please enter the infrix equation")
l = len(n)
s = [0]*l
for x in range (l):
    if (n[x] == "^"):
        s[x] = 5
    elif (n[x] == "/" ):
        s[x] = 4
    elif (n[x] == "*" ):
        s[x] = 3
    elif (n[x] == "+"):
        s[x] = 2
    elif (n[x] == "-"):
        s[x] = 1
    elif (n[x] == "("):
        s[x] = "("
    elif (n[x] == ")"):
        s[x] = ")"
    else:
        s[x] = n[x]
print(s)
o1 = 0
p1 = 0
o2 = 0
for x in range (l):
    if (s[x] == "(" or s[x] == ")" or s[x] == 1 or s[x] == 2 or s[x] == 3 or s[x] == 4 or s[x] == 5):
        o2 = o2+1
    else:
        p1 = p1+1
o = [6]*o2
p = [0]*p1
#6 is considered as a blank space
o1 = 0
p1 = 0
for x in range (l):
    if (s[x] == 1):
        if (o[o1 - 1] != 1 or o[o1 - 1] != 2 or o[o1-1] < 1 ):
            o[o1] = 1
            o1 = o1 + 1
        else:
            print (o[o1],end="1")
            o[o1] = 6
            o1 = o1-1
    elif (s[x] == 2):
        if (o[o1 - 1] != 2 or o[o1 - 1] != 1 or o[o1-1] < 2 ):
            o[o1] = 2
            o1 = o1 + 1
        else:
            print (o[o1],end="1")
            o[o1] = 6
            o1 = o1-1
    elif (s[x] == 3):
        if (o[o1 - 1] != 3 or o[o1 - 1] != 4 or o[o1-1] < 3 ):
            o[o1] = 3
            o1 = o1 + 1
        else:
            print (o[o1],end="1")
            o[o1] = 6
            o1 = o1-1
    elif (s[x] == 4):
        if (o[o1 - 1] != 4 or o[o1 - 1] != 3 or o[o1-1] < 4 ):
            o[o1] = 4
            o1 = o1 + 1
        else:
            print (o[o1],end="1")
            o[o1] = 6
            o1 = o1-1
    elif (s[x] == 5):
        if (o[o1 - 1] != 5 or o[o-1] < 5):
            o[o1] = 5
            o1 = o1 + 1
        else:
            print (o[o1],end="1")
            o[o1] = 6
            o1 = o1-1
    elif (s[x] == "("):
        o[o1] = "("
        o1 = o1+1
    elif (s[x] == ")"):
        while (o[o1] != "("):
            if (o[o1] == 1):
                print ("-",end="")
            elif (o[o1] == 2):
                print("+", end="")
            elif (o[o1] == 3):
                print("*", end="")
            elif (o[o1] == 4):
                print("/", end="")
            elif (o[o1] == 5):
                print("^", end="")
            else:
                print("",end="")
            o[o1] = 6
            o1 = o1-1
        o[o1] = 6
    elif (s[x] != "(" and s[x] != ")" and s[x] != 1 and s[x] != 2 and s[x] != 3 and s[x] != 4 and s[x] != 5):
        print(s[x],end="")
for x in range (o2):
    if (o[o2-1] == 6):
        print ("",end="")
        o2 = o2-1
    else:
        if (o[o2-1] == 1):
            print("-", end="")
        elif (o[o2-1] == 2):
            print("+", end="")
        elif (o[o2-1] == 3):
            print("*", end="")
        elif (o[o2-1] == 4):
            print("/", end="")
        elif (o[o2-1] == 5):
            print("^", end="")
        o2 = o2-1