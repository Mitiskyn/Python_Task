# Пользователь вводит текст(строка). Словом считается последовательность 
# непробельных символов идущих подряд, слова разделены одним пробелом. 
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells
# I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells

# Output: 13

line = (input('Введите символы строки через пробел: ').lower().split())
result = [i.strip('.,?!\n').lower() for i in line]
result = set(result)
print(result)
print(len(result))

# print(len(set(input("Введите текст: ").lower().split())))