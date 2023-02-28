def linear (a,i,ch,p):
    if (i <= len(a)):
        if (a[i] == ch):
            print ("Value present")
            p = 1
        else:
            i = i+1
            return (linear(a,i,ch,p))
    else:
        if (p == 0):
            print ("Value not present")
import array as arr