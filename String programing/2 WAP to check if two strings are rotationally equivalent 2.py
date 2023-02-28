n = input ("Please enter the first word")
m = input ("Please enter the second word")
temp = 0
for y in range (1,len(n)):
    x = n[y:len(n)]+n[0:y]
    if (x==m):
        temp = temp+1
if (temp >0):
    print ("It is Rotational equivalent")
else:
    print("It is not rotational equivalent")