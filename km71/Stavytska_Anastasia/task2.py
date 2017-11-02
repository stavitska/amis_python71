
 while(1):
  x1 = float (input('Введіть довжину катета x1:'))
  if x1<=0: print('введіть чісло більше 0')
  else:
      print('x1:' ,x1)
      break

while(2):
  x2 = float (input('Введіть довжину катета x2:'))
  if x2 <= 0: print('введіть чісло більше 0')
  else:
      print('x2:', x2)
      break


  y = (x1*x2/2)
  print ( 'Площа - ', y)

