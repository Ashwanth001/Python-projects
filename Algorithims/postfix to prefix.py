n = input ("Please enter the inrix equation")
l = len(n)
operand = ""
operator = ""
exp = ""
for x in range (l):
    if (n[x] != ")"):
        if (n[x] != "-" and n[x] != "+" and n[x] != "*" and n[x] != "/" and n[x] != "^"):
            operand = operand+n[x]
            print(operand)
        else:
            operator= n[x]+operator
            print(operator)
print(operator+operand)