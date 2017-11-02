while 1:
    while (1):
            try:
             x = int(input('Введіть ціле чісло'))
            except ValueError:
             print('число має бути цілим')
             break
            else:

                print('The next number for the number', x, 'is' ,x+1, '.','\n','The previous number for the number', x, " is ", x-1, ".", '\n')

                z = input('Press any key for repeat or "E" for exit')
                if (z == 'E' or z == 'e'):

                     break

