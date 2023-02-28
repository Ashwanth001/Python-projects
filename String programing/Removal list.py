n = input("Please enter the sentence")
l = int(input("Please enter how many words"))
l1 = len(n)+1
a = [""]*l
s = [""]*l1
w = ""
n = n+" "
for x in range (l):
    print(x)
    a[x] = input("Please enter the word")
count = 0
for y in range (l1):
    if (n[y] == " "):
        s[count] = w
        count = count+1
        w = ""
    else:
        w = w+n[y]
w = ""
p = 0
for x in range (len(s)):
    for y in range (len(a)):
        if (s[x] == a[y]):
            p = p+1
            print(a[y], "is present")
            print()
    if (p == 0):
        print(s[x]," ",end="")
    else:
        p = 0
