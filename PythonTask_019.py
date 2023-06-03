n = [int(i) for i in input().split()]
k = int(input("Введите кол-во сдвигов: "))
result_list = [n[i - k] for i in range(len(n))]
print(result_list)