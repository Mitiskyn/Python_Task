# Вводится десятичное число. Реализовать алгоритм его перевода в двоичную
# систему счисления через рекурсию. Нельзя использовать функцию bin()

# *Пример:*
#     10
#     *Вывод:*
#     1010

n = int(input("Введите число: "))
b = ''

while n > 0:
    b = str(n % 2) + b
    n = n // 2
print(b)