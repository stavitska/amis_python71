a1=int(input("введіть номер рядку ,де знаходиться тура "))
b1=int(input("введіть номер стовпчика ,де знаходиться тура"))
a2=int(input("введіть номер рядку ,куди повинна переміститися тура"))
b2=int(input("введіть номер стовпчика ,куди повинна переміститися тура"))
if a1==a2 or b1==b2:
    print('yes')
else:
    print('no')