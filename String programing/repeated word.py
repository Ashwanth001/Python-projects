n = input("Please enter the word")
g = input ("Please enter the 2nd word(It should be 4 or less characters and shouldn't be repeated)")
g0 = g[0]
g1 = g[1]
g2 = g[2]
g3 = g[3]
ga = 0
gb = 0
gc = 0
gd = 0
c = 0
for x in (n):
    if (x == g0):
        ga = ga+1
    elif (x == g1):
        gb = gb+1
    elif (x == g2):
        gc = gc + 1
    elif (x == g3):
        gd = gd + 1
while (ga > 0 or gb > 0 or gc > 0 or gd > 0):
    ga = ga-1
    gb = gb-1
    gc = gc-1
    gd = gd-1
    c = c+1
print ("The word ",g,"is repeated",c-1,"times")