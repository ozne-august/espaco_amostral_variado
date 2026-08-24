import random
from itertools import product

Site = {
    "cores": ["azul", "verde", "vermelho", "amarelo"],
    "fontes": ["Arial", "Times New Roman", "Verdana"],
    "plataformas": ["Web", "Mobile"]
}

# Espaço amostral
S = list(product(*config.values()))
print(combinacoes)

# Tamanho do espaço amostral
tamanho_S = print(len(combinacoes))

# Experimento aleatório
resultado = random.choice(combinacoes)
print(selecao)