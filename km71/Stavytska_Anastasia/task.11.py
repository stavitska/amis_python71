
import math

a1=int(input("введіть номер рядку першої клітини "))
b1=int(input("введіть номер стовпчика першої клітини"))
a2=int(input("введіть номер рядку другої клітини"))
b2=int(input("введіть номер стовпчика другої клітини"))
if a1-a2==math.fabs(3) and b1-b2==math.fabs(1) or a1-a2==math.fabs(1) and b1-b2==math.fabs(3):
    print('yes')
else:
    print('no')