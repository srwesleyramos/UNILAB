import os
import time

candidato_nome_1 = None
candidato_numero_1 = None
candidato_nome_2 = None
candidato_numero_2 = None

votos_first = 0
votos_second = 0
votos_branco = 0
votos_nulos = 0

started = False
options = None

while True:
    os.system('cls')

    print()
    print("Esse é um simulador de eleição")
    print()
    print("Escolha a ação desejada:")
    print("    (1) Cadastrar novo candidato")
    print("    (2) Iniciar a votação")
    print("    (3) Apresentar resultados")
    print("    (0) SAIR")
    print()

    options = input(">> ")

    if options == '1':
        if started:
            print("Essa ação está proibida pois já houve uma votação!")
            time.sleep(3)
            continue

        if candidato_nome_2 is not None:
            print("Os candidatos já foram cadastrados!")
            time.sleep(3)
            continue

        if candidato_nome_1 is None:
            candidato_nome_1 = input('Nome do primeiro candidato: ')
            candidato_numero_1 = input('Número do primeiro candidato: ')
        else:
            candidato_nome_2 = input('Nome do segundo candidato: ')
            candidato_numero_2 = input('Número do segundo candidato: ')

        print("O candidato foi cadastrado com sucesso.")

    elif options == '2':
        if started:
            print("Essa ação está proibida pois já houve uma votação!")
            time.sleep(3)
            continue

        if candidato_nome_2 is None:
            print("Essa ação está proibida pois não há candidatos suficientes!")
            time.sleep(3)
            continue

        while True:
            os.system('cls')

            print()
            print("Escolha o candidato desejado:")
            print(f"    ({candidato_numero_1}) {candidato_nome_1}")
            print(f"    ({candidato_numero_2}) {candidato_nome_2}")
            print("    (BB) Branco")
            print("    (00) Nulo")
            print("    (.) Encerrar votação")
            print()

            options = input(">> ")

            if options == candidato_numero_1:
                votos_first += 1
            elif options == candidato_numero_2:
                votos_second += 1
            elif options == 'BB':
                votos_branco += 1
            elif options == '00':
                votos_nulos += 1
            elif options == '.':
                started = True
                break
            else:
                print("Você deve escolher uma opção válida.")

            print("Voto cadastrado com sucesso!")
            time.sleep(3)

    elif options == '3':
        if not started:
            print("Essa ação está proibida pois não houve uma votação!")
            time.sleep(3)
            continue

        total = votos_first + votos_second + votos_branco + votos_nulos

        if votos_first != votos_second:
            winner = candidato_nome_1

            if votos_second > votos_first:
                winner = candidato_numero_2

            print()
            print("O candidato " + winner + " ganhou a eleição!")
        else:
            print()
            print("Não houve um vencedor nessa eleição, tivemos um empate!")

        print()
        print(" - " + candidato_nome_1 + ": " + str(votos_first) + " (" + str(100 * votos_first / total)[:5] +"%)")
        print(" - " + candidato_nome_2 + ": " + str(votos_second) + " (" + str(100 * votos_second / total)[:5] +"%)")
        print(" - Brancos e nulos: " + str(votos_branco + votos_nulos) + " (" + str(100 * (votos_branco + votos_nulos) / total)[:5] +"%)")
        print()
        break

    elif options == '0':
        print("Te vejo em breve!")
        break
    else:
        print("Você deve escolher uma opção válida.")

    time.sleep(3)
