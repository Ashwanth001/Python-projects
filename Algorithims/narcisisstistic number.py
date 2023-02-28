n = int(input("Please enter the digit"))
i = 0
l = 0
cn = n
t = 0
cn1 = n
while (n > 0):
    i = n%10
    n = n-i
    n = n/10
    l = l+1
y = 0
t = 0
while (cn > 0):
    y = cn%10
    c = y**l
    cn = cn-y
    cn = cn/10
    t = t+c
if (t == cn1):
    print ("It is a narcissististic number")
else:
    print ("It is not a narcissististic number")