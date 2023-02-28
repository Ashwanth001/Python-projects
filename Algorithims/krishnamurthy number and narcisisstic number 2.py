def narcisissitc_number (n):
    i = 0
    l = 0
    cn = n
    t = 0
    cn1 = n
    while (n > 0):
        i = n % 10
        n = n - i
        n = n / 10
        l = l + 1
    y = 0
    t = 0
    while (cn > 0):
        y = cn % 10
        c = y ** l
        cn = cn - y
        cn = cn / 10
        t = t + c
    if (t == cn1):
        print("It is a narcissististic number")
    else:
        print("It is not a narcissististic number")
def krishnamurthy_number (n):
    cn = n
    i = 0
    l = 1
    s = 0
    while (n > 0):
        i = n % 10
        for x in range(1, int(i + 1)):
            l = l * x
        s = s + l
        l = 1
        n = n - i
        n = n / 10
    if (cn == s):
        print("It is a krishnamurthy number")
    else:
        print("It is not a krishnamurthy number")
n = int(input("Please enter the input"))
narcisissitc_number(n)
krishnamurthy_number(n)
# Algorithm
# Narcissistic number:
#Step1: Find the length of the digit
#Step2: Extract each digit and power it to the length of the number
#Step3: Add everything and check if it is a Narcissitic number
# Krishnamurthynumber
#Step4: Find the factorial of each digit
#Step5: Add it all up
# Step6: Check if it is a Krishnamurty
#Step7: Check if it is both or not both Krishnamurty number or a narcissistic number