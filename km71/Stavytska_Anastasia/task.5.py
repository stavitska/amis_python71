a=int(input("введіть перше число"))
b=int(input("введіть друге число"))
c=int(input("введіть третє число"))
if a==b==c:
    print("3")
elif a==b or a==c or b==c:
    print("2")
else:
    print("0")