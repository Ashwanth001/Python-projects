n = int(input("Please enter the length of the queue"))
push = 0
pop = 0
empty = 0
peek = 0
size = 0
exit = 0
f = 0
b = 0
a = [0]*n
x = 0
p = 0
k = 0
while (exit == 0):
    print("Enter 1 for push")
    print("Enter 2 for pop")
    print("Enter 3 for empty")
    print("Enter 4 for peek")
    print("Enter 5 for size")
    if (push == 1 or pop == 1 or empty == 1 or peek == 1 or size == 1 or exit == 1):
        print("Enter 6 for exit")
    ch = int(input("Please enter the choice"))
    if (ch == 1):
        if (b != n ):
            j = int(input("Please enter the value"))
            a[b] = j
            b = b+1
            print (a)
            print ("1")
        else:
            while (a[x] == 0 and p == 1):
                x = x+1
                if (a[x] == 0):
                    p = 1
            a[x] = int(input("Please enter the value"))
            print (a)
            b = x
            print ("2")
            b = b+1
    elif (ch == 2):
        if (f == -1):
            print("The queue is underflowed")
        else:
            a[f] = 0
            print (a)
    elif (ch == 3):
        a = [0] * n
        empty = 1
        b = -1
        print (a)
    elif (ch == 4):
        print (a[b])
        print (a[f])
        peek = 1
        print (a)
    elif (ch == 5):
        print (b)
        size = 1
        print (a)
    elif (ch == 6):
        exit = 1
        print (a)