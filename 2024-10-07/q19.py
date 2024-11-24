x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

print('Lista de números primos nesse intervalo:')

for i in range(x, y + 1):
    if i > 2:
        j = 0

        for k in range(i, 0, -1):
            if i % k == 0:
                j += 1

        if j == 2:
            print(' - ', i)