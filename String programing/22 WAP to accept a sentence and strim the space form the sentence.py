n = input ("Please enter the sentence")# inputing the sentence
w= ""#initializeing the variable
for x in n:
    if (x == " "):
        w = w# checking if there is any space
    else:
        w = w+x#continuing the sentence
print (w)#printing out the sentence
