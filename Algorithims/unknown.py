n1 = input ("PLease enter the number")
n = int (n1)
d = 0
s = 0
cont = 1
while (cont == 1):
    while (n > 0):
        d = n%10
        n = (n-d)/10
        s = s+d
    if (s <=9):
        cont = 0
    else:
        n= s
        d = 0
        s = 0
print ("The answer is ",s)