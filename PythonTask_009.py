n = int(input ("Введите факториал числа:  "))
i = 1
result = 1
while i <= n:
    result *= i
    i +=1
print(f'{n}! = {result}')