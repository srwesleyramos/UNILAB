nome = input("Informe o seu nome: ")
temp = ""

index = 0
write = True

while (index < len(nome)):
    if (write):
        temp += nome[index] + "."

    write = nome[index] == ' '
    index += 1

print(temp)