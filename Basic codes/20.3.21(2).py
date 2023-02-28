n1 = input ("Enter a number")
n = int (n1)
s = 0
while (n!=0):
    s=s+n
    n1 = input ("Enter 0 to exit or enter another number to add to the sum")
    n = int(n1)
print ("Your total sum is",s)
