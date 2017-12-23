def u(a):
    if (len(a)==1):
        return a[0]
    else:
        return min(u(a[:-1]), a[-1])

d=[2, -3, 5, 1]
y=u(d)
print(y)

