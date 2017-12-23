def distance(x1, y1, x2, y2):
    a=((x2-x1)**2+(y2-y1)**2)**(1/2)
    return a
x1=float(input("введіть коордінату х1"))
x2=float(input("введіть коордінату х2"))
y1=float(input("введіть коордінату у1"))
y2=float(input("введіть коордінату y2"))
b=distance(x1, y1, x2, y2)
print(b)