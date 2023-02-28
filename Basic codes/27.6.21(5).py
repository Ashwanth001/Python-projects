m = input("please enter the lower case and UPPER CASE mixture")
n = ""
ox = 0
for x in m:
    ox = ord(x)
    if (ox >= 65 and ox <= 90):
        n = n+x
    elif (ox >= 97 and ox <= 122):
        n = x+n
print (n)
