import time

maxima = 6
qtd = 0
opcao = None

while True:
    print("""
Este é um simulador de ônibus

Escolha a ação desejada:
    (1) Entrar um passageiro
    (2) Descer um passageiro
    (3) Informar a ocupação atual
    (0) SAIR
""")

    opcao = int(input("Escolha: "))

    if opcao == 1:
        if qtd < maxima:
            qtd += 1
        else:
            print("O ônibus se encontra lotado!")
    elif opcao == 2:
        if qtd > 0:
            qtd -= 1
        else:
            print("O ônibus se encontra vázio!")
    elif opcao == 3:
        print("A lotação atual é: " + str(qtd) + "/6")
    elif opcao == 0:
        break
    else:
        print("Opção inválida!")

    time.sleep(3)