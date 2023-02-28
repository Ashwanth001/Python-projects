def prime_number (n):
    p = 0
    for x in range (1,n+1):
        if (n % x == 0):
            p = p+1
    if (p > 2):
        print ("It is not a prime number")
    else:
        print ("It is a prime number")
def prime_factorial (m):
    f = 1
    for x in range (1,m+1):
        f = f*x
    print (f)
z = int(input("Please enter the value"))
c = int(input("Enter 1 for prime number and 2 for factorial"))
if (c == 1):
    prime_number(z)
else:
    prime_factorial(z)