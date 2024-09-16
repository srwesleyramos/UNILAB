##
## Escolhendo o personagem
##

player_display_1 = None
player_health_1 = 100
player_target_1 = 200

player_display_2 = None
player_health_2 = 100
player_target_2 = 200

player_display_3 = None
player_health_3 = 100
player_target_3 = 200

_index = 0

while (_index != game_players):
    time.sleep(2)
    os.system("cls")

    _index += 1

    print(f"           ___________________________________{globals()[f"ASCII_NUMBER_{_index}_LINE_1"]}____ ")
    print(f"  ________|    ____  _                        {globals()[f"ASCII_NUMBER_{_index}_LINE_2"]}   |________")
    print(f"  \\       |   |  _ \\| | __ _ _   _  ___ _ __  {globals()[f"ASCII_NUMBER_{_index}_LINE_3"]}   |       /")
    print(f"   \\      |   | |_) | |/ _` | | | |/ _ \\ '__| {globals()[f"ASCII_NUMBER_{_index}_LINE_4"]}   |      /")
    print(f"    \\     |   |  __/| | (_| | |_| |  __/ |    {globals()[f"ASCII_NUMBER_{_index}_LINE_5"]}   |     /")
    print(f"    /     |   |_|   |_|\\__,_|\\__, |\\___|_|    {globals()[f"ASCII_NUMBER_{_index}_LINE_6"]}   |     \\")
    print(f"   /      |_________________ |___/ ___________{globals()[f"ASCII_NUMBER_{_index}_LINE_7"]}___|      \\")
    print(f"  /__________)                                {globals()[f"ASCII_NUMBER_{_index}_LINE_8"]}(__________\\")
    print()
    print(f"    Você deve escolher o nome do seu personagem. Certifique-se")
    print(f"  de ser maior que 3 e menor que 6 caracteres.")
    print()

    _name = input("  >> ")

    if (len(_name) > 2 and len(_name) < 7):
        globals()[f"player_display_{_index}"] = _name
    else:
        print("\n  O nome fornecido não respeita as regras estabelecidas.")
        _index -= 1
