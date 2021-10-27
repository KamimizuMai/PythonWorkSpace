multiplication = [i*j for i in range(1, 3) for j in range(1, 10)]

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 6, 8, 10, 12, 14, 16, 18] 
print(multiplication)

multiplication = []

for i in range(1, 3):
    for j in range(1, 10):
        multiplication.append(i*j)

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(multiplication)
