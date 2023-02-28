ac = 0
while (ac == 0):
    n = input ("Please enter the password")
    l = len(n)
    if (l > 8):
        ox = 0
        uc = 0
        lc = 0
        d = 0
        sc = 0
        s = 0
        for x in (n):
            ox = ord(x)
            if (ox >= 65 and ox <= 90):
                uc = uc+1
            elif (ox >= 97 and ox <= 122):
                lc = lc+1
            elif (ox >= 48 and ox <= 57):
                d = d+1
            elif (ox == 32):
                s = s+1
            else:
                sc = sc+1
        if (uc >= 1 and lc >= 1 and d >= 1 and sc >= 1 and s == 0):
            print ("Password accepted")
            ac = 1
        else:
            print ("Password invalid")
            print ("Please try again")
            print (sc)
    else:
        print ("Password invalid")
        print ("Please try again")