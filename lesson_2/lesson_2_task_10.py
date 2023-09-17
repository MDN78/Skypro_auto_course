
def bank(x, y):
    i = 0
    while i < y:
        x += (x * 0.1)
        i += 1
    return x

print(bank(100, 10))
        
        