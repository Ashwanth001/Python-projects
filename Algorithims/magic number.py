n = int (input ("Please enter the input"))
d = n
a = 1
while (d >= 10):
    a = d%10
    d = d-a
    d = d/10
    d = d+a
if (d == 1):
    print ("It is a magic number")
else:
    print ("It is not a magic number")
