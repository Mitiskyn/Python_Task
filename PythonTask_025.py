line = input('Введите символы строки через пробел: ').split() # создаем список, пользователь вводит 
res = {}                                                      # создаем словарь
for i in line:                                                # циклом по списку
    if i in res:                                              # заполняем словарь, где символ=ключ
        print(f'{i}_{res[i]}', end='  ')
    else:
        print(f'{i}_{0}', end='  ')
    res[i] = res.get(i, 0)+1