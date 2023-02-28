#WAP to accept an 2D array from the user and to use binary serach to replace the element from which the user provided with the value that the user also provides
r = int(input("Please enter the number of rows"))
c = int(input("Please enter the number of columns"))
a=[]
for x in range (r):
    b=[]
    for y in range (c):
        b.append(int(input()))
    a.append(b)
print("Inputed matrix:")
for x in range (r):
    for y in range (c):
        print(a[x][y],end=" ")
    print()

i=0
temp = [0]*r*c

for x in range (r):
    for y in range (c):
        temp[i] = a[x][y]
        i = i+1

l = len(temp)

s = int(input("Please enter the element to be replaced"))
n = int(input("Please enter the value that is to be replaced with the desired element"))

for z in range (0,l-1):
    min = temp[z]
    pos = z
    for y in range(z+1,l):
        if (temp[y] < min):
            min = temp[y]
            pos = y
    swap = temp[z]
    temp[z] = temp[pos]
    temp[pos] = swap

uv = l-1
lv = 0
m = int((uv+lv)/2)
while (lv < uv):
    if (temp[m] == s):
        temp[m] = n
    elif (temp[m] < s):
        lv = m+1
        m = int((lv+uv)/2)
    else:
        uv = m-1
        m = int((lv+uv)/2)
i = 0

for x in range (r):
    for y in range (c):
        a[x][y] = temp[i]
        i = i+1

print("Outputed matrix:")

for x in range (r):
    for y in range (c):
        print(a[x][y],end=" ")
    print()

