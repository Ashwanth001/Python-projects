n = input ("Please enter the word")
w = ""
v = ""
for x in n:
    if (x == "a" or x == "A"):
        w = w+"*"
        v = v+"a"
    elif (x == "e" or x == "E"):
        w = w+"*"
        v = v +"e"
    elif (x == "i" or x == "I"):
        w = w+"*"
        v = v +"i"
    elif (x == "o" or x == "O"):
        w = w+"*"
        v = v + "o"
    elif (x == "u" or x == "U"):
        w = w+"*"
        v = v + "u"
    else:
        w= w+x
print(w)
print(v)