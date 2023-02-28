n = int(input("Please enter the length of the queue"))
f = 0
b = 0
a = [0]*n
push = 0
pop = 0
empty = 0
peek = 0
size = 0
exit = 0
while (exit == 0):
    print("Enter 1 for push")
    print("Enter 2 for pop")
    print("Enter 3 for empty")
    print("Enter 4 for peek")
    print("Enter 5 for size")
    if (push == 1 or pop == 1 or empty == 1 or peek == 1 or size == 1 or exit == 1):
        print ("Enter 6 for exit")
    ch = int(input("Please enter your choice"))
    if (ch == 1):
        push = 1
        if (f == n):
            print ("The queue is overflowed")
            print(a)
        else:
            a[f] = int(input("Please enter the value"))
            f = f+1
            print(a)
    elif (ch == 2):
        pop = 1
        if (f == b):
            print ("The queue is underflowed")
            print(a)
        else:
            for x in range (0,f-1):
                a[x] = a[x+1]
            a[f-1] = 0
            f = f-1
            print(a)
    elif (ch == 3):
        empty = 1
        a = [0] * n
        f = 0
        b = 0
        print(a)
    elif (ch == 4):
        peek = 1
        print ("First value: ",a[b])
        print ("The last value",a[f-1])
        print(a)
    elif (ch == 5):
        size = 1
        print (f)
        print(a)
    elif (ch == 6):
        print (a)
        print ("The queue is finished")
        exit = 1
