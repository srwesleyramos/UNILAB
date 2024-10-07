nome = input("Informe o seu nome: ")

index = len(nome) - 1

while (index >= 0):
    if (nome[index] == ' '):
        break
    index -= 1

print(nome[index + 1:])