n = input ("Please enter the word")
l1 = len(n)
l = l1-1
l2 = l1
h = 1
for x in range (l1):
     for y in range (h):
         print (n[l],end="")
         l = l+1
     h = h+1
     l2=l2-1
     l = l2-1
     print ()