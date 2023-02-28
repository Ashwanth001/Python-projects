n = input ("Please enter the sentence")
r1 = input ("Please enter 1 for presenting in ratio or 2 for percentage")
r = int(r1)
v = 0
c = 0
s = 0
v1 = 0
c1 = 0
l = len(n)
for x in n:
    if (x == "a" or x == "A"):
        v = v+1
    elif (x == "e" or x == "E"):
        v = v+1
    elif (x == "i" or x == "I"):
        v = v+1
    elif (x == "o" or x == "O"):
        v = v+1
    elif (x == "u" or x == "U"):
        v = v+1
    elif (x == " "):
        s = s+1
    else:
        c = c+1
c = c-s
if (r == 1):
    print ("The ratio of vowels to consonants is",v,":",c)
else:
    v1 = v/l*100
    c1 = c/l*100
    print ("The percentage of vowels is",v1,"%")
    print("The percentage of consonants is", c1, "%")