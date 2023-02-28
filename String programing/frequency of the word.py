s = input ("Please enter the sentence")
fw= input ("please enter the word you want to find")
w = ""
f = 0
for x in (s):
    if (x == " "):
        if (w == fw):
            f = f+1
        w = ""
    else:
        w = w+x
print ("The frequency of the word is",f)
