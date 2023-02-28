n = int (input ("Please enter the length of the array "))
a = [0]*n
for x in range (n):
    print ("Location number",x+1)
    a[x] = int(input ())
s = int (input ("Please enter the search element"))
e = 0
for x in range (n):
    if (s == a[x]):
        e = e+1
print ("Number of occurrences of the number",s,"in the said array:",e)