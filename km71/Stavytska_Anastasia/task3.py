def count(list,i,counter): #Використовуємо для знаходження кільк. ел. в групах
	if i < len(list):
		m = findGroup(list,i,0,1)
		if counter < m[0]: #Знаходження найбільшої групи із всіх
			counter = m[0]
		return count(list,i + 1,counter)
	else:
		return counter    


def findGroup(list,i,indicator,k): #Використовуємо для знаходження груп
	if i < len(list) - 1 and list[i] == list[i + 1]: #Перевірка на однаковість сусідніх елементів
		k = k + 1        
		return findGroup(list,i + 1,indicator,k)
	else :
		return k,indicator


list = input("please write a list ").split()
print(count(list,0,0))