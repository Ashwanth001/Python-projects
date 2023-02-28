def push (f,b,push2,a,n):
    fbp = int(input ("Please enter 1 for front push and 2 for rear push"))
    push1 = 1
    if (fbp == 1):
        if (f == b):
            print ("The queue is overflowed")
        else:
            w = f
            for x in range (f):
                a[w] = a[w-1]
                w = w-1
            a[f] = int(input("Please enter the value"))
            f = f+1
        print (a)
    else:
        if (f == b):
            print ("The queue is overflowed")
        else:
            e = b
            for x in range (b-f):
                a[e-1] = a[e]
                e = e-1
            a[b] = int(input("Please enter the value"))
            b = b-1
        print (a)
    return (f,b,push2,a,n)


def pop (pop2,a,n,f,b):
    fbp = int(input("Please enter the 1 for front pop and 2 for rear pop"))
    if (fbp == 1):
        if (a[0] == 0):
            print ("The queue is underflowed")
        else:
            a[0] = 0
        f = f-1
    else:
        if (a[n-1] == 0):
            print ("The queue is underflowed")
        else:
            a[n-1] = 0
        b = b+1
    print (a)
    pop2 = 1
    return (pop2,a,n,f,b)


def empty (a,n,empty2,f,b):
    a = [0]*n
    print (a)
    empty2 = 1
    f = 0
    b = n-1
    return (a,n,empty2,f,b)


def peek (a,f,peek2,b):
    print ("The front value is",a[f])
    print ("The rear value is",a[b])
    peek2 = 1
    return (a,f,peek2,b)


def size (f,b,size2):
    print ("The size of the queue is ",f+b)
    size2 = 1
    return (f,b,size2)


def exit (exit2,a):
    exit2 = 1
    print (a)
    return (exit2,a)


push1 = 0
pop1 = 0
empty1 = 0
peek1 = 0
size1 = 0
exit1 = 0
l = int(input("Please enter the length of tre value"))
c = [0] * l
b1 = l-1
f1 = 0


#fbp = front or back push
#f = f1 (front indicator)
#b = b1 (back indicator)
#push1,pop1,ect = push2,pop2 (indicators)
#a = c (array)
#n = l(length of the array)


while (exit != 0):
    print("Enter 1 for push")
    print("Enter 2 for pop")
    print("Enter 3 for empty")
    print("Enter 4 for peek")
    print("Enter 5 for size")
    if (push1 == 1 or pop1 == 1 or empty1 == 1 or peek1 == 1 or size1 == 1 or exit1 == 1):
        print("Enter 6 for exit")
    ch = int(input("Please enter the choice"))
    if (ch == 1):
        f1,b1,push1,c,l = push(f1,b1,push1,c,l)
    elif (ch == 2):
        pop1,c,l,f1,b1 = pop(pop1,c,l,f1,b1)
    elif (ch == 3):
        c,l,empty1,f1,b1 = empty(c,l,empty1,f1,b1)
    elif (ch == 4):
        c,f1,peek1,b1 = peek(c,f1,peek1,b1)
    elif (ch == 5):
        f1,b1,size1 = size(f1,b1,size1)
    elif (ch == 6):
        exit1,c = exit(exit1,c)
