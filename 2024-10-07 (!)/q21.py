import os
import random

n = 9
t = 1

while n != 0:
    i = random.randint(1, n)
    j = int(input(f'Digite o número que você acha que é (entre 1 e {n}): '))

    if i == j:
        print('Você ganhou, parabéns!')
        break
    else:
        os.system('cls')

        print()
        print('Você errou :(')
        print()
        print(' - Número de tentativas:', t)
        print(' - Intervalo: 1 à', n)
        print(' - Número sorteado:', i)
        print(' - Número selecionado:', j)
        print()

    t += 1
    n -= 1

if n == 0:
    print('Você perdeu o jogo!')