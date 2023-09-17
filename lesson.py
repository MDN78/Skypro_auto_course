# file for training

# for i in range(1, 21):
#     print(f"X = {i}, and X2 = {i ** 2}")
 
# print("*"*50)

# students = ["Ivan", "Petr", "Serg", "Olga"]

# for i in students:
#     print(i)

# for x in range(0, len(students)):
#     print(students[x])

# print("*"*50)

# word = "Test"
# for s in word:
#     print(s)
    
# print("*"*50)

# # напечатать только четные

# nums = [1,2,3,4,5,6,7,8,9,]
# for i in nums:
#     if (i % 2 != 1):
#         print(i)
        
# user_login = 'adam'
# user_pass = 'qwer1234'

# login = input('Login: ')
# password = input('Password: ')

# if (login == user_login) and (password == user_pass):
#     print('Success')
# else:
#     print('Locked')

crit_1 = "red"
crit_2 = "lock"

color = input('Color: ')
feature = input('Feature: ')

if color == "red" or feature == "lock":
    print("I've got it!")
else:
    print("Let's check something else...")