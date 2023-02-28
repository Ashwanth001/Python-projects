d1 = input ("Please enter the bill")
d = int(d1)
t = 0
while (d!=0):
    t = t+d
    d1 = input ("Enter 0 to stop or add more lists")
    d = int(d1)
print ("The total bill is ",t)