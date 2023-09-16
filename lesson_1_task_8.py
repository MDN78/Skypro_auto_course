list = []

def add_to_list(num):
    list.append(num)
    return list

for i in range(11):
    add_to_list(num=input())

print(*list)