# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# *Пример:*

# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Размер шоколадки в высоту: "))
m = int(input("Размер шоколадки в длину: "))
k = int(input("Сколько хотим сделать прямоугольничков: "))

if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('Шоколадку можно разломить на прямоугольнички :)')
else:
    print('Шоколадку нельзя разломить :(')