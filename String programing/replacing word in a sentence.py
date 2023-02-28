p = input ("Please enter the paragraph")
ws = input ("Please enter the word you want to switch")
wr = input ("Please enter the word you wanna replace with")
p = p+" "
w = ""
n = ""
for x in (p):
    if (x == " "):
        if (w == ws):
            n = n+" "+wr
        else:
            n = n+" "+w
        w = ""
    w = w+x
print (n)