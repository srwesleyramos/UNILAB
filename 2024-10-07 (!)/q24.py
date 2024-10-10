menor = None
maior = None

n = int(input('Por favor, me informe a quantidade de números: '))

for i in range(0, n):
    j = int(input('Por favor, me informe um número: '))

    if menor is None:
        menor = j
        maior = j
    else:
        menor = min(menor, j)
        maior = max(maior, j)

print('O menor número é:', menor)
print('O maior número é:', maior)