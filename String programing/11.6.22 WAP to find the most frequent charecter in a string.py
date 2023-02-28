n = input ("Please enter the sentence")
f = 0
c = 0# inputing the sentence
w= ""#initializeing the variable
for x in n:
    if (x == " "):
        w = w# checking if there is any space
    else:
        w = w+x#continuing the sentence
for x in w:
    for z in w:
        if (x == z):
            c = c+1
    if (c > f):
        f = c
        l = x
    c = 0
print (l)
print (f)