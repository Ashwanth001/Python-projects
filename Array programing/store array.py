def store_array (n):
    l = 0
    p = 0
    c = 0
    cn = n
    k = 0
    q = 1
    while (n > 0):
        l = n%10
        n = n-l
        n = n/10
        c = c+1
    a = [0]*c
    while (cn > 0):
        l = cn%10
        cn = cn-l
        cn = cn/10
        p = l
        a[k] = p
        k = k+1
    for x in range(c):
        b = [0]*c
        b[x] = a[len(a)-q]
        q = q+1
        print(b[x])
n = int(input("Please enter the digits"))
store_array(n)