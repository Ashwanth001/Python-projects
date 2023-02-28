n = input ("Please enter the paragraph")
c1 = input ("PLease enter the 1st character")
c2 = input ("Please enter the 2nd character")
w = ""
for x in (n):
    if (x == c1):
        w = w+c2
    elif (x == c2):
        w = w+c1
    else:
        w = w+x
print (w)