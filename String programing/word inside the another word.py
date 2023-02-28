sw = input ("PLease enter the word")
iw = input ("Please enter the word you want inside the another word")
lsw = len(sw)
m = 0
n =""
if (lsw % 2 == 0):
    m = lsw/2
else:
    m = (lsw+1)/2
m = int(m)
for x in range (0,m):
    n = n+sw[x]
n = n + iw
for x in range (m,lsw):
    n = n+sw[x]
print (n)
