x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

soma = 0

for i in range(x, y + 1):
    soma += i

print('A soma desse intervalo é', soma)

impares = 0

print('Os números impares nesse intervalo são:')

for i in range(x + 1, y):
    if i % 2 == 1:
        impares += 1
        print(' - ', i)

    if impares == 3:
        break

pares = 0

print('Os últimos números pares nesse intervalo são:')

for i in range(y - 1, x, -1):
    if i % 2 == 0:
        pares += 1
        print(' - ', i)

    if pares == 2:
        break
