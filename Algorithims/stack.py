def push (a,i):
    a[i+1] = int(input("Please enter a number"))
    print(a)
    i = i+1
    return(i)
def pop (a,i):
    x = a[i]
    a[i] = 0
    i = i-1
    print(a)
    if (c <= 0):
        print ("The stack is underflowed")
    return (i)
def empty (a,i):
    a = [0]*l
    i = 0
    print(a)
    return(i)
def peek (a,i):
    print(a[i])
    p = a[i]
    return(i)
def size (a):
    print(len(a))
    return (a)
def exit (a):
    print(a)
    return (a)
l = int(input("Please enter the length of the stack"))
s = [0]*l
c = -1
y = 0
while (y != 1):
    print("1-Push\n2-Pop\n3-Empty\n4-Peek\n5-Size\n6-Exit")
    ch=int(input("Please enter the choice"))
    if (ch == 1):
        c = push(s,c)
    elif (ch == 2):
        c = pop(s,c)
    elif(ch == 3):
        c = empty(s,c)
    elif(ch == 4):
        c = peek(s,c)
    elif (ch == 5):
        c = size(s)
    else:
        c = exit(s)
#step1: display menu with options
#step2:wait for user input
#step3:if push then ask for input
#step4 if pop then remove the last element
#step5: if empty then remove every element
#step6: if peek then print the last element
#step7: if size then print number of elements in it
#step8 if exit print the stack and end it