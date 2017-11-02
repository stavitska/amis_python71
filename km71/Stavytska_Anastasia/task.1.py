a = []
n = int(input("введіть кількість учнів"))
for i in range(n):

   while 1:
       c=int(input('введіть зріcт учня'))

       if c>200:
         print('введіть зріст < 200')
       else:
           a.append(c)
           break


a.sort()
a.reverse()
print(a)
h = int(input("введіть зріст нового учня"))
N=n
for j in range(n):
    if h>a[j]:
        N=j+1
        break
print(N)









