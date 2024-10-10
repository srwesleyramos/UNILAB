menor = None
maior = None

for i in range(0,4):
    j = int(input('Por favor, me informe um número: '))

    if menor is None:
        menor = j
        maior = j
    else:
        menor = min(menor, j)
        maior = max(maior, j)

print('O menor número é:', menor)
print('O maior número é:', maior)