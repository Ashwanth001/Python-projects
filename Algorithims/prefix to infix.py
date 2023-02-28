n = input("Please enter the equation")
l = len(n)
operand = [0]*l
stack = [0]*l
f = ""
o = -1
for x in range (l):
    stack[l-1] = n[x]
    l = l-1
l = len(n)
for x in range (l):
    if (stack[x] != "/" and stack[x] != "*" and stack[x] != "+" and stack[x] != "-"):
        o = o+1
        operand[o] = stack[x]
    else:
        f = "("+operand[o]+stack[x]+operand[o-1]+")"
        operand[o] = 0
        o = o-1
        operand[o] = f
        f = ""
print(operand[0])