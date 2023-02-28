l1 = input ("PLease enter the input: ")
l = int (l1)
i = 1
j = 1
while (i<=l):
    if (i == 1 or i == l):
        while (j <=l):
            print ("* ",end="")
            j = j+1
        j = 1
    else:
        while (j <= l):
            if (j == 1 or j == l):
                print("* ", end="")
            else:
                print ("  ",end="")
            j = j + 1
        j = 1
    i = i+1
    print ()