n = int(input("Please enter the digit"))
cn = n
i = 0
l = 1
s = 0
while (n > 0):
    i = n%10
    for x in range (1,int(i+1)):
        l = l*x
    s = s+l
    l = 1
    n = n-i
    n = n/10
if (cn == s):
    print ("It is a krishnamurthy number")
else:
    print ("It is not a krishnamurthy number")