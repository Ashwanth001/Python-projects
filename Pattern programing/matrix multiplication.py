print("Matrix1")
r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))

matrix1 = []
print("Enter the entries rowise:")

for x in range(r):
    a = []
    for y in range(c):
        a.append(int(input()))
    matrix1.append(a)

print ("Matrix 1: ")
for x in range(r):
    for y in range(c):
        print(matrix1[x][y], end=" ")
    print()

print("Matrix2")
r1 = int(input("Enter the number of rows:"))
c1 = int(input("Enter the number of columns:"))

while (c != r1):
    r1 = int(input("Enter the number of rows:"))
    c1 = int(input("Enter the number of columns:"))

matrix2 = []
print("Enter the entries rowise:")

for x in range(r1):
    a = []
    for y in range(c1):
        a.append(int(input()))
    matrix2.append(a)

print ("Matrix 2: ")
for x in range(r1):
    for y in range(c1):
        print(matrix2[x][y], end=" ")
    print()

temp = 0
temp1 = 0

print("Result: ")

for x in range (r):
    for y in range (c1):
        for z in range (c):
            temp = matrix1[x][z] * matrix2[z][y]
            temp1 = temp1+temp
        print (temp1,end=" ")
        temp1 = 0
    print()
