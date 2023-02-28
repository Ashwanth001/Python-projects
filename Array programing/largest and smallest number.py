n = int (input("Please enter the length of the array"))
a = [0]*n
for x in range (0,n):
    print ("The location number",x+1)
    a[x] = int (input ("Please enter the value"))
s = 0
l1 = 0
l = 0
s2 = 0
l2 = 0
for y in range (n):
    l = a[y]
    if (l > l1):
        l1 = l
s1 = l1
for z in range (n):
    s = a[z]
    if (s < s1):
        s1 = s
si = 0
li = 0
for b in range(0,n):
    if (a[b] == s1):
        si = b
    elif (a[b] == l1):
        li = b
print ("The largest number of the array is ",l1," and its index position is",li)
print("The smallest number of the array is ", s1, " and its index position is",si)