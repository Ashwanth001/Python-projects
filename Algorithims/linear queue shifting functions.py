def push (a,f,m):
    push1 = 1
    if (f == m):
        print("The queue is overflowed")
        print(a)
        return (f)
    else:
        a[f] = int(input("Please enter the value"))
        f = f + 1
        print(a)
        return (f,push)
def pop (a,f,b):
    pop1 = 1
    if (f == b):
        print("The queue is underflowed")
        print(a)
        return(f)
    else:
        for x in range(0, f - 1):
            a[x] = a[x + 1]
        a[f - 1] = 0
        f = f - 1
        print(a)
        print(f)
    return (f,pop)
def exit (a,f):
    print(a)
    print("The queue is finished")
    exit1 = 1
f1 = 0
def empty (a,f):
    empty = 1
    a = [0] * n
    f = 0
    print(a)
    return (f,empty)
def peek (a,f,b):
    peek1 = 1
    print("First value: ",a[b])
    print("The last value",a[f-1])
    print(a)
    return (f,b)
def size (a,f):
    print (f)
    size1 = 1
b1 = 0
n = int(input("Please enter the length of the value"))
s = [0]*n
while (exit != 1):
    print("Enter 1 for push")
    print("Enter 2 for pop")
    print("Enter 3 for empty")
    print("Enter 4 for peek")
    print("Enter 5 for size")
    if (push == 1 or pop == 1 or empty == 1 or peek == 1 or size == 1 or exit == 1):
        print ("Enter 6 for exit")
    ch = int(input("Please enter the choice"))
    if (ch == 1):
        f1 = push(s,f1,n)
    elif (ch == 2):
        f1 = pop(s,f1,b1)
    elif(ch == 3):
        f1 = empty(s,f1)
    elif(ch == 4):
        f1 = peek(s,f1,b1)
    elif (ch == 5):
        f1 = size(s,f1)
    else:
        f1 = exit(s,f1)
#step1: create functions for push and more
#step2: return the count variable
#step3: create if funtions for each functions