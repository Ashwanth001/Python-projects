s = input ("Please enter the sentence")
r = input ("Please enter the word you want to remove")
wx = ""
fs = ""
for x in s:
    if (x == " "):
        wx = ""
    else:
        wx = wx+x
        if (wx != r):
            print (wx,end="")
        else:
            wx = ""

