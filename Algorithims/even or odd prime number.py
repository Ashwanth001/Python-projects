l1 = input ("Please enter the number")
l = int(l1)
p = 1
f = 0
if (l % 2 != 0):
        while (p <=l):
            if (l % p == 0):
                f = f+1
            p = p+1
        if (f == 2):
            print ("It is a prime number as well as an odd number")
        else:
            print ("It is not a prime number but it is an odd number")
else:
    print ("It is an even number and not a prime number")
