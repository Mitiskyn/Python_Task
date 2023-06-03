# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
#     Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной
# во входном файле грядки.

# Input:
# 4 -> 1 2 3 4

# Output:
# 9

import random
bush = int(input("Введите количество кустов: "))
berryes = list(random.randint(0, 10) for i in range(bush))
result = []
i = 0

print(f"{bush} -> {berryes}")

if bush <= 0:
    print("Кусты отсутствуют")
elif bush == 1:
    print(f"Максимальный урожай {berryes[0]}")
elif bush == 2:
    sum = berryes[0] + berryes[1]
    print(f"Максимальный урожай {sum}")
else:
    while (i < bush):
        if (i == bush - 1):
            sum = berryes[i] + berryes[i - 1] + berryes[0]
        else:
            sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
            result.append(sum)
            result.sort()
        i += 1
    print(f"Максимальный урожай {result[-1]}")