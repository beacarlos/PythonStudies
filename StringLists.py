import random

names = ["David", "Marcos", "Erik", "Igor", "Monark", "Bruno", "Williaw", "Victor", "Emerson", "Pedro"]

N1 = random.choice(names)
N2 = random.choice(names)
N3 = random.choice(names)

phrase = f"Os 3 vencedores do sorteio são da plataforma do discord são: {N1}, {N2}, {N3}"

print(phrase)
names.pop()
print(names)