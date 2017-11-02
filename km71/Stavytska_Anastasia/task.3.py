firstNamber=input("введіть перше ціле число")
secondNamber=input("введіть друге ціле число")
thirdNamber=input('введіть третє ціле число')
a=(int(firstNamber))
b=(int(secondNamber))
c=(int(thirdNamber))
if a<b and a<c :
    print("найменше число:", a)
elif b<a and b<c:
    print("найменше число:", b)
else:
    print("найменше число:", c)
