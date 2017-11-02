a = []
n = int(input("введіть кількість елементів"))
for i in range(n):
    a.append(int(input('введіть число')))

b=[]
for j in range(n):

    d=a.count(a[j])
    b.append(d)

c=[]
for k in range(n):
    if b[k]==1:
        c.append(a[k])
print(c)

