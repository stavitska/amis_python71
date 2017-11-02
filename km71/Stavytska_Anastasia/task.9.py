import math
a1=int(input("введіть номер рядку першої клітини "))
b1=int(input("введіть номер стовпчика першої клітини"))
a2=int(input("введіть номер рядку другої клітини"))
b2=int(input("введіть номер стовпчика другої клітини"))
if math.fabs(a1-a2)==math.fabs(b1-b2):
    print('yes')
else:
    print('no')