# Нажать кнопку Run Python file для выполнения скрипта

list = []

def add_to_list(num):
    list.append(num)
    return list

for i in range(11):
    counter = 1
    add_to_list(num=input(f"Необходимо ввести 11 чисел. Введите число № {i + 1}: "))
    
print(*list)