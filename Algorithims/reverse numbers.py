n1 = input ("PLease enter the number")
n = int(n1)
t = 0
r = 0
while (n > 0):
    t = n % 10
    r = r*10
    r = r+t
    n = n-t
    n = n/10
print (int(r))