n =input ("PLease enter the input")
ord1 = 0
up = 0
lo = 0
sp = 0
for x in n:
    ord1 = ord(x)
    if (ord1 >= 97 and ord1 <= 122):
        lo = lo+1
    elif (ord1 >= 65 and ord1 <= 90):
        up = up+1
    else:
        sp = sp+1
print ("Lower case",lo)
print ("Upper case",up)
print ("Special charecters",sp)