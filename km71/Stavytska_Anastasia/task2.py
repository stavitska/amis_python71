def Max(list): #Знаходимо максимальний елемент
    global a
    if len(list) == 1:
        a = list[0]
    else:
        a = max(int(Max(list[:-1])), int(list[-1]))
    return a

def count(list): #Друга функція для знаходження кількості максимальних ел.
	Max(list)
	return list.count(str(a)) #Знаходимо за допомогою .count()
print(count(input("please write a list ").split())) 