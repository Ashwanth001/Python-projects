d1 = input ("Please enter the number")
d = int (d1)
t = 0
r = 0
while (d > 0):
    t = d % 10
    r = (r * 10)
    r = (r + t)
    d = d - t
    d = d/10
print(int (r))
