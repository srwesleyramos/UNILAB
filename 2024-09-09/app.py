import math
import time

print("")
print("Exercício da Calculadora")
print("  by @srwesleyramos")
print("")

while True:
    print()
    print("Escolha uma opção abaixo:")
    print("  1 - somar")
    print("  2 - subtrair")
    print("  3 - multiplicar")
    print("  4 - dividir")
    print("  5 - bhaskara")
    print("  0 - sair")
    print()

    options = int(input("Digite sua opção: "))

    if (options > 0) and (options < 5):
        n1 = int(input("\nDigite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        if options == 1:
            print("Resultado da soma:", n1 + n2)
        elif options == 2:
            print("Resultado da subtração:", n1 - n2)
        elif options == 3:
            print("Resultado da multiplicação:", n1 * n2)
        elif options == 4:
            if n2 == 0:
                print("Resultado da divisão:", 0)
            else:
                print("Resultado da divisão:", n1 / n2)

    elif options == 5:
        # x² + x - 1 = 0

        a = int(input("\nDigite o valor de A: "))
        b = int(input("Digite o valor de B: "))
        c = int(input("Digite o valor de C: "))

        # -b +- √b² -4ac

        if (a != 0) and (b != 0) and (c != 0):
            delta = math.pow(b, 2) - 4 * a * c

            if delta < 0:
                print("Não existe raizes reais.")
                time.sleep(3)
                continue

            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)

        elif (a != 0) and (b != 0):
            x1 = +math.sqrt((-b) / a)
            x2 = -math.sqrt((-b) / a)

        elif (a != 0) and (c != 0):
            x1 = 0
            x2 = -c / a

        else:
            x1 = 0
            x2 = 0

        print("Resultado do X¹:", x1)
        print("Resultado do X²:", x2)

    elif options == 0:
        print("O programa foi encerrado!")
        break

    else:
        print("Opção inválida.")

    time.sleep(3)
