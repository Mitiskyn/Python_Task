n = int(input ("Введите числа:"))
n0 = 0
a0 = 0
a1 = 1
i = 2
while n0 < n:
    n0 = a0 + a1
    a0 = a1
    a1 = n0
    i += 1
    if n0 > n:
        i = 0
if i != 0:
    print(i)
else:
    print (-1)
