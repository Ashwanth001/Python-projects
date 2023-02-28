n = int(input ("Please enter the length of the array"))
a = [0]*n
c = 1
for x in range (n):
    a[x] = int(input ("Please enter the value"))
for y in range (0,n):
    for z in range (0,n-y-1):
        print (c)
        c = c+1
        if (a[z] > a[z+1]):
            swap = a[z+1]
            a[z+1] = a[z]
            a[z] = swap
        print (a)
for b in range (n):
    print (a[b],end=" ")
#step1:Input the array
#Step2:Select the first value and check if it is greater than the next value
#Step3:If greater then swap two of them and then check the next number and keep going until the end(
#Step4:Check again from the first value until the number we finished sorting

