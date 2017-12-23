def check1(n):
	try : # перевіряємо на правильність введених данних
		n = int(n)
		if n >= 1:
			k = True
		else:
			k = False			
	except :
		k = False
	return k	


def check2(x):
	try : # перевіряємо на правильність введених данних
		x = float(x)
		k = True		
	except :
		k = False
	return k


def calc(n,x): # функція для підрахунків
	sum = 0
	if n == 0:
		return 0
	else:
		n = int(n) #переводимо n і x в числовий формат
		x = float(x)
		return n/(x*x + 1)**0.5+calc(n-1,x)	#підрахунки за формулою


def run():#Виконуємо тестування 
	n = input('Будь ласка, введіть значення "n" ')
	x = input('Будь ласка, введіть значення "x" ')
	print(check1(n))
	print(check2(x))
	if check1(n)==check2(x)==True:#Якщо перші 2 функції вірні, то є сенс використовувати наступну
		print(calc(n,x))
	else:
		print("False")	
run()		