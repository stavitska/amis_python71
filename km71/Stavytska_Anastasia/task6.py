while 1:
 x1=int(input('введіть кількість учнів у першій групі'))
 x2=int(input('введіть кількість учнів у другій групі'))
 x3=int(input('введіть кількість учнів у третій групі'))

 y=x1%2+x2%2+x3%2+x1//2+x2//2+x3//2
 print('мінімальна кількість столів',y)
 z = input('Press any key for repeat or "E" for exit')
 if (z == 'E' or z == 'e'):
              break

