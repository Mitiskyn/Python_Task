# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input('Введите первый элемент арифметической прогрессии: '))
d = int(input('ВВедите разность между ее членами: '))
n = int(input('Введите количество членов прогрессии: '))

def rec(n):
    if n ==0:
        return 0
    return (a + d*(n-1))

list = []              
for i in range(1,n+1):
    list.append(rec(i))
print(*list)           