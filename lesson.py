# get rating
rate = int(input("Add your rating from 1 - 5 "))

# check rating from 1 til 5
if rate < 1:
    rate = 1


if rate > 5:
    rate = 5

feedback = ''

if rate == 1:
    feedback = input(" Express your opinion ")
elif rate == 2:
    feedback = input("WHF fellow!?! ")
elif rate == 3:
    feedback = input("so-so, let's check your problem ")
else:
    print("OK")
    
print(rate)
print(feedback)
    
