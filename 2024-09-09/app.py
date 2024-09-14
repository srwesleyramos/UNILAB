print("")
print("Exercício da Calculadora")
print("  by @srwesleyramos")
print("")

while (True):
    print("Escolha uma opção abaixo:")
    print("  1 - somar")
    print("  2 - subtrair")
    print("  3 - multiplicar")
    print("  4 - dividir")
    print("  0 - sair")

    op = int(input("Digite sua opção: "))
    
    if (op > 0 and op < 5):
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        if (op == 1):
            print("Resultado da soma:", n1 + n2)
        elif (op == 2):
            print("Resultado da subtração:", n1 - n2)
        elif (op == 3):
            print("Resultado da multiplicação:", n1 * n2)
        elif (op == 4):
            print("Resultado da divisão:", n1 / n2)
    elif (op == 0):
        print("O programa foi encerrado!")
        break;
    else:
        print("Opção inválida.")