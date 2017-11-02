import math

x=[]
y=[]
for i in range(8):
    print('введіть координати %d-го ферзя' %(i+1))
    x.append(int(input("")))
    y.append(int(input("")))

res="No"

for j in range(8):
    c=x[j]
    d=y[j]
    for k in range(8):
        if k!=j:
            if x[k]==c or y[k]==d:
                res= 'yes'
                break
    if res == 'yes':
        break

if res=="No":
    for m in range(8):
        a=x[m]
        b=y[m]
        for n in range(8):
            if n!=m:
                if math.fabs(x[n]-a)==math.fabs(y[n]-b):
                    res='yes'
                    break
        if res=='yes':
            break
print(res)

