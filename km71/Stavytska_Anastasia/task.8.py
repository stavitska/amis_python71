a1=int(input("введіть номер рядку першої клітини "))
b1=int(input("введіть номер стовпчика першої клітини"))
a2=int(input("введіть номер рядку другої клітини"))
b2=int(input("введіть номер стовпчика другої клітини"))
if a1-a2==1 and b1==b2 or a2-a1==1 and b1==b2 or b2-b1==1 and a1==a2 or b1-b2==1 and a1==a2 or a1-a2==1 and b1-b2==1 or a2-a1==1 and b2-b1==1 or a1-a2==1 and b2-b1==1 or a2-a1==1 and b1-b2==1:
    print ("yes")
else :
    print ("no")