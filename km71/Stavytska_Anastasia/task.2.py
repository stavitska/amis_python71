a = []
n = int(input("введіть кількість елементів"))
for i in range(n):
    a.append(int(input('введіть число')))
b = []
for j in range(n):

    d=a.count(a[j])
    b.append(d)
m=0
for k in range(n):

    if b[k] == 2:
        m=m+1
print("кількість пар з однаковими елементами:",m/2)

