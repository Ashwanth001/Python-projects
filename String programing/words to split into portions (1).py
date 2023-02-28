t = 0
while (t != 1):
    n = input("Please enter the word you want to split")
    p1 = input("Please enter the how many portions you want to split")
    p = int (p1)
    l = len(n)
    if (l % p == 0):
        t = 1
    if (t == 1):
        d = l/p
        w = ""
        for c in range (0,l):
            x= len(w)
            if (x == d):
                print (w)
                w = ""
                w = w+n[c]
            else:
                w = w+n[c]
print (w)