n = input ("Please enter the input")
c = n
t = len(n)
r  = "!"
for x in range (t-1,-1,-1):
    r = r+(n[x])
if (r == n):
    print ("It is not a palindrome")
else:
    print ("It is a palindrome")