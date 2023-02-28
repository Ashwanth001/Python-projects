push = 0
pop = 0
empty = 0
peek = 0
size = 0
exit = 0
l = int(input("Please enter the length of the stack"))
a = [0]*l
c = 0
while (exit != 1):
    print ("Enter 1 for push")
    print ("Enter 2 for pop")
    print ("Enter 3 for empty")
    print ("Enter 4 for peek")
    print ("Enter 5 for size")
    if (push == 1 or pop == 1 or empty == 1 or peek == 1 or size == 1 or exit == 1):
        print ("Enter 6 for exit")
    n = int(input ("Please enter the value"))
    if (c == l):
        c = c-1
    if (n == 1):
        c = push(s,c)
    elif (n == 2):
        pop = 1
        if (c != -1):
            a[c] = 0
            c = c-1
        else:
            print ("THE STACK IS UNDERFLOWED")
            print()
            print()
    elif (n == 3):
        empty = 1
        a = [0] * l
        c = -1
    elif (n == 4):
        peek = 1
        r = a[c-1]
        print (r)
    elif (n == 5):
        size = 1
        print (c)
    elif (n == 6):
        exit = 1
        print("You have exited the stack")
    print(a)
def push (a,i):
    a[i+1] = int(input("Please enter a number"))
    print(a)
    i = i+1
    return(i)
s = [0]*l
i = 0
c = -1
#