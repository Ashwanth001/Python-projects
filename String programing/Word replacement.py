n = input ("Please enter the sentence")
h = input ("Please enter the word you want to replace")
i = input ("Please enter the word you want to replace with")
w = ""
n = n+" "
for x in n:
    if (x != " "):
        w = w+x
    else:
        if (w == h):
            print (i,end=" ")
            w = ""
        else:
            print (w,end=" ")
            w = ""