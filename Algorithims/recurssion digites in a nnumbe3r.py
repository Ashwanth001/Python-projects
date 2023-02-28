def digits_in_num (n,l):
    i = n % 10
    l = l + 1
    n = n - i
    n = n / 10
    if (n == 0):
        return l
    else:
        return (digits_in_num(n,l))
m = int(input("Please enter the digit"))
k = digits_in_num(m,0)
print (k)