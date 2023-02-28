def narcisist_number (n):
    l = 0
    j = 0
    cn = n
    pwrofn = 0
    i = 0
    while (n > 0):
        l = n%10
        n = n-l
        n = n/10
        j = j+1
    while (cn > 0):
        l = cn % 10
        cn = cn - l
        cn = cn / 10
        p = l
        for x in range (j):
            pwrofn = p*p
            i = i+p
    print(i)
n = int(input("Please enter the digit"))
narcisist_number(n)
def krishnammurthy_num (n):
    l = 0
    j = 0
    cn = n
    k = 1
    t = 0
    while (n > 0):
        l = n % 10
        n = n - l
        n = n / 10
    while (cn > 0):
        l = cn % 10
        cn = cn - l
        cn = cn / 10
        p = int(l)
        for x in range (p):
            j = j+k
            k = k+1
        t = t+j
        j = 0
    print(t)
krishnammurthy_num(n)