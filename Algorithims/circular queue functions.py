#f = f1(front indicator)
#b = b1(back indicator
#n = l(length of queue)
#push2,pop2 etc = push1,pop1(indicators)
#a = c queue (array)
def push (b,push2,n,a):
    if (b != n):
        x = 0
        p = 0
        j = int(input("Please enter the value"))
        a[b] = j
        b = b + 1
        print(a)
        print("1")
    else:
        while (a[x] == 0 and p == 1):
            x = x + 1
            if (a[x] == 0):
                p = 1
        a[x] = int(input("Please enter the value"))
        print(a)
        b = x
        print("2")
        b = b + 1
    push2 = 1
    return (b,push2,n,a)
def pop (f,a,pop2):
    if (f == -1):
        print("The queue is underflowed")
    else:
        a[f] = 0
        print(a)
    pop2 = 1
    return (f,a,pop2)
def empty (a,n,empty2):
    a = [0] * n
    empty2 = 1
    b = -1
    print(a)
    return (a,n,empty2)
def peek (a,b,f,peek2):
    print(a[b])
    print(a[f])
    peek2 = 1
    print(a)
    return (a,b,f,peek2)
def size (b,a,size2):
    print(b)
    size2 = 1
    print(a)
    return (b,a,size2)
def exit (exit2,a):
    exit2 = 1
    print (a)
    return (exit2)
push1 = 0
pop1 = 0
empty1 = 0
peek1 = 0
size1 = 0
exit1 = 0
l = int(input("Please enter the length of tre value"))
c = [0]*l
b1 = 0
f1 = 0
#f = f1(front indicator)
#b = b1(back indicator
#n = l(length of queue)
#push2,pop2 etc = push1,pop1(indicators)
#a = c queue (array)
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
        b1,push1,l,c = push(b1,push1,l,c)
    elif (ch == 2):
        f1,c,pop1 = pop (f1,c,pop1)
    elif (ch == 3):
        c,l,empty1 = empty(c,l,empty1)
    elif (ch == 4):
        c,b1,f1,peek1 = peek (c,b1,f1,peek1)
    elif (ch == 5):
        b1,c,size1 = size (b1,c,size1)
    else:
        exit1,c = exit (exit1,c)