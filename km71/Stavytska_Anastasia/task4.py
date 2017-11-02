
while(1):
       try:
            N = int(input('Введіть кількість студентів'))

       except ValueError:
            print('кількість учнів має бути цілим числом')

       else:
            if (N<=0):
                print('введіть чісло більше 0')
            else:
                print('кількість учнів', N)
                break

while(1):
       try:
            K = int(input('Введіть кількість яблук'))
       except ValueError:
            print('кількість яблук має бути цілим числом')
       else:
            if (K < 0):
                print('введіть чісло більше або рівне 0')
            else:
                print('кількість яблук', K)
                break
a = K//N
b = K%N
print('кожному учню', a, 'яблук' '\n','залишилося в кошику', b,'яблук' )
