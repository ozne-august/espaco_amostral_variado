n = 6  # pessoas na fila

num_arranjos = 1
for i in range(1, n + 1):
    num_arranjos *= i

print(num_arranjos)