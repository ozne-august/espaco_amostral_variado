import random
from itertools import product

config = {
    "cores": ["azul", "verde", "vermelho", "amarelo"],
    "fontes": ["Arial", "Times New Roman", "Verdana"],
    "plataformas": ["Web", "Mobile"]
}

# Espaço amostral
combinacoes = list(product(*config.values()))
print(combinacoes)

# Tamanho do espaço amostral
print(len(combinacoes))

# Experimento aleatório
selecao = random.choice(combinacoes)
print(selecao)