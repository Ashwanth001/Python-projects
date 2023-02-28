s = input ("Please enter the sentence")
s = s+" "
f = ""
rw = ""
w = ""
for x in (s):
    if (x == " "):
        l = len(w)
        l = l-1
        while (l >= 0):
            rw = rw+w[l]
            l = l-1
        f = f+" "+rw
        w = ""
        rw = ""
    else:
        w = w+x
print (f)