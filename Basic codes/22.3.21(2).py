d1 = input ("Please enter the number ")
d = int(d1)
nine = 0
z = 0
z = (d % 10)
nine = z
d = d - nine
d = d / 10
d = int(d)

print ("The last place of the number is ",nine,".And the remaining number left is ",d,".")
