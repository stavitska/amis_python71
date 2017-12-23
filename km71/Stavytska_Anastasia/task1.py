def Max(list): #Знаходимо максимальний елемент
    global a
    if len(list) == 1:
        a = list[0]
    else:
        a = max(int(Max(list[:-1])), int(list[-1]))
    return a


def secondMax(list):
	Max(list)
	list.remove(str(a)) #Видаляємо 1 максимальний елемент
	Max(list) #Шукаємо 2 максимальний елемент
	return(str(a))#Використовуємо str щоб не отримати у відповідь None


print(secondMax(input("please write a list ").split()))