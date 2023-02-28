n = int (input ("Please enter the input"))
t = 0
c = 0
h = 0
l = 0
cpy = n
while (n > 0):
    t = n%10
    n = n-t
    n = n/10
    c = c+1
n = cpy
t = 0
sum = 0
while (n > 0):
    t = n%10
    n = n-t
    n = n/10
    sum = sum+(t**c)
if (cpy == sum):
    print ("It is a narcissistic number")
else:
    print("It is not a narcissistic number")
#Step1:Take in the input and find the length of it
#Step2:And raise it to the length for each digit
#Step3:Check if it is the same