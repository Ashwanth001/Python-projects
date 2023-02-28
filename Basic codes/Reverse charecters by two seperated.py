n = input ("Please enter the input in even number of characters")
l= len(n)
w= ""
for x in range (1,l+1,2):
    w = w+n[x]
    w = w+n[x-1]
    w = w+" "
print (w)