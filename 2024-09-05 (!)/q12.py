nome = input("Informe o seu nome: ")

index = 0
count = 0

while (index < len(nome)):
    if (nome[index] == 'a' or nome[index] == 'A'):
        count += 1
    index += 1

print(count)