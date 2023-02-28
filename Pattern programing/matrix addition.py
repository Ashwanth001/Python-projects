r = int(input("Enter the number of rows:"))
c = int(input("Enter the number of columns:"))

matrix1 = []
print("Enter the entries rowwise:")

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

matrix2 = []
print("Enter the entries rowwise:")

for x in range(r):
    a = []
    for y in range(c):
        a.append(int(input()))
    matrix2.append(a)

print ("Matrix 2: ")
for x in range(r):
    for y in range(c):
        print(matrix2[x][y], end=" ")
    print()

matrix3 = []

for x in range (r):
    a = []
    for y in range (c):
        a.append(matrix1[x][y]+matrix2[x][y])
    matrix3.append(a)

print ("Matrix 3: ")
for x in range(r):
    for y in range(c):
        print(matrix3[x][y], end=" ")
    print()

