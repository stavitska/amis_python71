while 1:
 N=int(input('введіть кількість хвилин після півночі'))
 N=int(N%1440)
 print(N // 60, N % 60)
 z = input('Press any key for repeat or "E" for exit')
 if (z == 'E' or z == 'e'):
    break