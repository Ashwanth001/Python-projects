s = input ("Please enter the sentence")
rd = input ("Please enter the word you want to remove or replace")
si = 0
s = s+" "
while (si != 1 or si != 2):
    si = int(input("Please enter 1 for deleting the word or 2 for replacing it"))
    w = ""
    fs = ""
    for x in s:
        if (x == " "):
            if (w == rd):
                if (si == 2):
                    r = input ("Please enter the replacement word")
                    w = r
                elif (si == 1):
                    w = ""
                fs = fs+w+" "
                w = ""
            else:
                fs = fs+w+" "
                w = ""
        else:
            w = w+x
    print (fs)