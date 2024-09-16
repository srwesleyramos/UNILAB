##
## Configuração dos players
##

game_players = None

while (True):
    time.sleep(2)
    os.system("cls")

    print("           __________________________________________        ")
    print("  ________|    ____  _                              |________")
    print("  \\       |   |  _ \\| | __ _ _   _  ___ _ __ ___    |       /")
    print("   \\      |   | |_) | |/ _` | | | |/ _ \\ '__/ __|   |      / ")
    print("    \\     |   |  __/| | (_| | |_| |  __/ |  \\__ \\   |     /  ")
    print("    /     |   |_|   |_|\\__,_|\\__, |\\___|_|  |___/   |     \\  ")
    print("   /      |_________________ |___/ _________________|      \\ ")
    print("  /__________)                                   (__________\\")
    print()
    print("    Selecione quantos jogadores irão participar. Certifique-se")
    print("  de usar o valor válido.")
    print()
    print("    Opções: 1, 2 ou 3.")
    print()

    _count = input("  >> ")

    if (_count == '1' or _count == '2' or _count == '3'):
        game_players = int(_count)
        break
    else:
        print("\n  Você inseriu um valor inválido, verifique e tente novamente.")
