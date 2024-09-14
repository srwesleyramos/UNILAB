##
## Escolhendo a dificuldade
##

difficulty_display = None
difficulty_damage = None
difficulty_speed = None

while (True):
    time.sleep(2)
    os.system("cls")

    print("           __________________________________________________________ ")
    print("  ________|    ____  _  __ _            _     _           _         |________")
    print("  \\       |   |  _ \\(_)/ _(_) ___ _   _| | __| | __ _  __| | ___    |       /")
    print("   \\      |   | | | | | |_| |/ __| | | | |/ _` |/ _` |/ _` |/ _ \\   |      /")
    print("    \\     |   | |_| | |  _| | (__| |_| | | (_| | (_| | (_| |  __/   |     /")
    print("    /     |   |____/|_|_| |_|\\___|\\__,_|_|\\__,_|\\__,_|\\__,_|\\___|   |     \\")
    print("   /      |_________________________________________________________|      \\")
    print("  /__________)                                                   (__________\\")
    print()
    print("    Escolha a dificuldade que você deseja para o jogo. Certifique-se de usar ")
    print("  o valor correspondente a desejada.")
    print()
    
    _index = 1

    while (f"DIFFICULTY_DISPLAY_{_index}") in globals():
        print(f"    {_index}:")
        print(f"      - Rótulo: {globals()[f"DIFFICULTY_DISPLAY_{_index}"]}")
        print(f"      - Força: {globals()[f"DIFFICULTY_DAMAGE_{_index}"]}")
        print(f"      - Esquivo: {globals()[f"DIFFICULTY_SPEED_{_index}"]}")
        print()
        
        _index += 1

    _difficulty = input("  >> ")

    if (f"DIFFICULTY_DISPLAY_{_difficulty}") in globals():
        difficulty_display = globals()[f"DIFFICULTY_DISPLAY_{_difficulty}"]
        difficulty_damage = globals()[f"DIFFICULTY_DAMAGE_{_difficulty}"]
        difficulty_speed = globals()[f"DIFFICULTY_SPEED_{_difficulty}"]

        print(f"\n  A dificuldade {difficulty_display} foi escolhida com sucesso!")
        break
    else:
        print("\n  Você inseriu um valor inválido, verifique e tente novamente.")