def factorial_number (n):
    if (n == 1):
        return n
    else:
        return n*factorial_number(n-1)
i = int(input("Please enter the digit"))
f = factorial_number(i)
print (f)