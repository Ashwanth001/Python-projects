n1 = input ("PLease enter the number")
n = int(n1)
t = 0
r = 0
while (n > 0):
    t = n % 10
    if (t == 5):
        r = r+1
    n = n-t
    n = n/10
print ("5 =",r)