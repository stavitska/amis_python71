def power(a, n):
    if n==1:
        b = a
    else:
        b = a*power(a,n-1)
    return b


while 1:
    g = float(input("введіть число: "))
    if g<=0:
        print("введіть число більше 0")

    else:
        break


while 1:
    k = int(input("введіть показник: "))
    if k<0:
      print("введіть невід'ємне число")
    else:
      break

l=power(g, k)
print(l)
