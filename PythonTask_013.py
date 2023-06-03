n = int(input ("Введите числа: "))
max_day_poristive = 0
count = 0
for i in range(n):
    x = int(input("Введите температруру дня: "))
    if x > 0:
        count += 1
    else:
        count = 0

    if max_day_poristive < count:
        max_day_poristive = count
print(max_day_poristive)




