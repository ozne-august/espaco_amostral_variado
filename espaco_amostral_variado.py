import math

n = 10  # botoes disponiveis (0 a 9)
r = 4   # botoes usados na senha

num_senhas = math.factorial(n) // math.factorial(n - r)

print(num_senhas)