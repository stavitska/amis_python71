m=int(input('введіть кількість клітин по вертикалі'))
n=int(input('введіть кількість клітин по горизонталі'))
k=int(input('введіть кількість клітин, яку ви бажаєте отримати'))

if k%m==0 or k%n==0:
    print('yes')
else:
    print('no')