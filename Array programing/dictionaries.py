#WAP a program to create a dictionary and perform operations using the following chart
#0. Add a value
#1. Change a value
#2. Delete a value
#3. Print all keys
#4. Print all values
#5. Print a particular value dependng to the key
#6. Delete all values
#7. Print key:value pairs
#8. Exit

n = 0

d = {}

while (n != 9):
    print("1. Enter 0 to add a value:\n2. Enter 1 to change a value:\n3. Enter 2 to delete a value:\n4. Enter 3 to print all keys\n5. Enter 4 to print all values\n 6. Enter 5 to print a particular value\n 7. Enter 6 to delete all values\n 8. Enter 7 to print key:value pairs\n 9. Enter 8 to exit ")
    n = int(input("Please enter your choice"))
    if n == 0:
        x = input("Please enter the key")
        y = input("Please enter the value")
        d.update({x:y})
        print(d)
    if n == 1:
        x = input("Please enter the key")
        y = input("Please enter the updated value")
        d[x] = y
        print(d)
    if n == 2:
        x = input("Please enter the key")
        d.pop(x)
        print(d)
    if n == 3:
        for x in d:
            print(x,end=" ")
        print()
    if n == 4:
        for x in d.values():
            print(x,end=" ")
        print()
    if n == 5:
        x = input("Please enter the key")
        print(d[x])
    if n == 6:
        d.clear()
        print(d)
    if n == 7:
        print(d)
    if n == 8:
        print(d)
        print("You have been exited")
