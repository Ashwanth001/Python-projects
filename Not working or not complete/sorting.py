n = int (input ("Please enter the length of the array"))
a = [0]*n
pos = 0
for x in range (0,n):
    print ("The location number",x+1)
    a[x] = int (input ("Please enter the value"))
for y in range (0,n-1):
    min = a[y]
    for z in range (y+1,n):
        if (a[z] < min):
            min = a[z]
            pos = a[z]
    swap = a[y]
    a[y] = min
    a[pos] = swap
for b in range (n):
    print (a[b],end=" ")
print ()
s = int (input ("Please enter the search element"))
ub = n
lb = 0
m = int((ub+lb)/2)
while (lb < ub):
    if (a[m] == s):
        print ("Element found at position",m+1)
        quit()
    elif (a[m] < s):
        lb = m+1
        m = int((lb+ub)/2)
    else:
        ub = m-1
        m = int((lb+ub)/2)
print ("The element was not present")
#Step1: Take the length of the array from the user and ask the value of each position indvidually
#Step2: Ask the user for the search element and create varaiables for the upper position, the lower position and the middle position
#Step3: Until the lower position is greater than the upper position check if the middle position is the search element.if true endthe program
#Step4: If not check if its position is less than the search element's position,if true ignore the poitions before the search middle position.Do the same if it is larger