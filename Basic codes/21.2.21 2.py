t1 = input ("Enter military time without colon")
t = int(t1)
if (t>=1200 and t<=2359):
    print ("The time is in pm")
elif (t<1200 and t>=0):
    print ("The time is in am")
else:
    print ("wrong input")