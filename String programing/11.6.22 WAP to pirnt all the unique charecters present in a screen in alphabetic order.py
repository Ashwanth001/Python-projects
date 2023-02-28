n = input ("Please enter the sentence")#inputing the sentence
w=""
temp = 0
for x in n:#extracting
    for z in w:
        if (x == z):#Checking if value present
            temp = temp +1
    if (temp == 0 ):#checking if value present in a another loop
        w = w+x#storing the string in a another variable
    temp = 0#reseting the value
a = len(w)*[0]#creating array
for x in range (len(w)):#convertimg string to array
    a[x] = w[x]#convertimg string to array
for y in range (len(a)):#convertion of string to ascii
    a[y] = ord(a[y])#convertion of string to ascii
for b in range (len(a)):#sorting
    for c in range (0,len(a)-b-1):#sorting
        if (a[c] > a[c+1]):#sorting
            swap = a[c]#sorting
            a[c] = a[c+1]#sorting
            a[c+1] = swap#sorting
for d in range (len(a)):#printing
    print (chr(a[d]))#printing