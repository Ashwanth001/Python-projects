n = int (input ("Please enter the input"))
c = 1
i = 0
cpy = n
e = 1
f = 0
while (n > 0):
    i = int (n%10)
    n = n-i
    n = n/10
    for x in range (i):
        c = c*e
        e = e+1
    f = f+c
    c = 1
    e = 1
if (cpy == f):
    print ("It is a Krishnamurthy Number")
else:
    print("It is not a Krishnamurthy Number")
#Step1:Take in the input and extract each number from it
#Step2:Multiply from 1 to the extracted digit from each value and add it all
#Step3:Check if the final vale is the same as the inputed value