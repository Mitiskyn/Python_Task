
n = int(input('Введите число: '))
max = n 
while n != 0:   
    n = int(input('Введите число: ')) 
    if n > max:
        max = n
print(f'Максимальное число в введнной последовательности: {max}')