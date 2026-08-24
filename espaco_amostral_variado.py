import random
from itertools import product

Site = {
    "cores": ["azul", "verde", "vermelho", "amarelo"],
    "fontes": ["Arial", "Times New Roman", "Verdana"],
    "plataformas": ["Web", "Mobile"]
}

# Espaço amostral
combinacoes = list(product(*Site.values()))
print("Espaço amostral:")
print(combinacoes)

# Tamanho do espaço amostral
tamanho_S = len(combinacoes)
print("Tamanho do espaço amostral:", tamanho_S)

# Experimento aleatório
resultado = random.choice(combinacoes)
print("Seleção aleatória:", resultado)