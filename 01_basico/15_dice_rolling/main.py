import random 

dados_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dados = []
total = 0

while True:
    num_de_dados = int(input("Quantos dados?\n> "))
    if num_de_dados <= 10:
        break
    else:
        print("\nMáximo 10 dados! Tente novamente.\n")
    

# numeros sorteados dos dados
for dado in range(num_de_dados):
    dados.append(random.randint(1, 6))

for linha in range(5):
    for dado in dados:
        print(dados_art.get(dado)[linha], end="")
    print()


for dado in dados:
    total += dado

print(f"\nTotal: {total}")
