import os
import random
import time

#
# CONFIGURAÇÕES
#

# TODO: balancear as armas e dificuldades

# Armas

WEAPON_DISPLAY_1 = "Arco e Flecha"
WEAPON_PRECISION_1 = 80
WEAPON_DAMAGE_1 = 20
WEAPON_SPEED_1 = 0.33

WEAPON_DISPLAY_2 = "Pistola"
WEAPON_PRECISION_2 = 40
WEAPON_DAMAGE_2 = 60
WEAPON_SPEED_2 = 0.23

WEAPON_DISPLAY_3 = "Bazuka"
WEAPON_PRECISION_3 = 10
WEAPON_DAMAGE_3 = 80
WEAPON_SPEED_3 = 0.13

# Dificuldade

DIFFICULTY_DISPLAY_1 = "Fácil"
DIFFICULTY_DAMAGE_1 = 20
DIFFICULTY_SPEED_1 = 0.7

DIFFICULTY_DISPLAY_2 = "Médio"
DIFFICULTY_DAMAGE_2 = 25
DIFFICULTY_SPEED_2 = 0.5

DIFFICULTY_DISPLAY_3 = "Díficil"
DIFFICULTY_DAMAGE_3 = 30
DIFFICULTY_SPEED_3 = 0.3

# Equipamento

# TODO: criar configuração dos equipamentos

#
# ASCII TEXT
#

# Numbers

ASCII_NUMBER_1_PART_1 = "___"
ASCII_NUMBER_1_PART_2 = " _ "
ASCII_NUMBER_1_PART_3 = "/ |"
ASCII_NUMBER_1_PART_4 = "| |"
ASCII_NUMBER_1_PART_5 = "| |"
ASCII_NUMBER_1_PART_6 = "|_|"
ASCII_NUMBER_1_PART_7 = "___"
ASCII_NUMBER_1_PART_8 = "   "

ASCII_NUMBER_2_PART_1 = "_______"
ASCII_NUMBER_2_PART_2 = " ____  "
ASCII_NUMBER_2_PART_3 = "|___ \\ "
ASCII_NUMBER_2_PART_4 = "  __) |"
ASCII_NUMBER_2_PART_5 = " / __/ "
ASCII_NUMBER_2_PART_6 = "|_____|"
ASCII_NUMBER_2_PART_7 = "_______"
ASCII_NUMBER_2_PART_8 = "       "

ASCII_NUMBER_3_PART_1 = "_______"
ASCII_NUMBER_3_PART_2 = " _____ "
ASCII_NUMBER_3_PART_3 = "|___ / "
ASCII_NUMBER_3_PART_4 = "  |_ \\ "
ASCII_NUMBER_3_PART_5 = " ___) |"
ASCII_NUMBER_3_PART_6 = "|____/ "
ASCII_NUMBER_3_PART_7 = "_______"
ASCII_NUMBER_3_PART_8 = "       "

# Objects

ASCII_TARGET_PART_1 = " .-. "
ASCII_TARGET_PART_2 = ". o ."
ASCII_TARGET_PART_3 = " ._. "
ASCII_TARGET_PART_4 = "  |  "

ASCII_TRAIL_PART_1 = "@"
ASCII_TRAIL_PART_2 = "#"

#
# APLICAÇÃO
#

print()
print("         _____  _    ____   ____ _____ _____")
print("        |_   _|/ \\  |  _ \\ / ___| ____|_   _|")
print("          | | / _ \\ | |_) | |  _|  _|   | |")
print("          | |/ ___ \\|  _ <| |_| | |___  | |")
print("     ____ |_/_/ __\\_\\_|_\\_\\\\____|_____|_|_|____")
print("    / ___|_   _|  _ \\|_ _| |/ / ____|  _ \\/ ___|")
print("    \\___ \\ | | | |_) || || ' /|  _| | |_) \\___ \\")
print("     ___) || | |  _ < | || . \\| |___|  _ < ___) |")
print("    |____/ |_| |_| \\_\\___|_|\\_\\_____|_| \\_\\____/")
print()
print("                  by @srwesleyramos")
print()

time.sleep(2)

# Escolhendo a dificuldade

difficulty_damage = None
difficulty_display = None
difficulty_speed = None

while True:
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

    while f"DIFFICULTY_DISPLAY_{_index}" in globals():
        print(f"    {_index}:")
        print(f"      - Título: {globals()[f"DIFFICULTY_DISPLAY_{_index}"]}")
        print(f"      - Força: {globals()[f"DIFFICULTY_DAMAGE_{_index}"]}")
        print(f"      - Esquivo: {globals()[f"DIFFICULTY_SPEED_{_index}"]}")
        print()

        _index += 1

    _difficulty = input("  >> ")

    if f"DIFFICULTY_DISPLAY_{_difficulty}" in globals():
        difficulty_damage = globals()[f"DIFFICULTY_DAMAGE_{_difficulty}"]
        difficulty_display = globals()[f"DIFFICULTY_DISPLAY_{_difficulty}"]
        difficulty_speed = globals()[f"DIFFICULTY_SPEED_{_difficulty}"]

        print(f"\n  A dificuldade {difficulty_display} foi escolhida com sucesso!")

        time.sleep(2)
        break
    else:
        print("\n  Você inseriu um valor inválido, verifique e tente novamente.")

    time.sleep(2)

# Escolhendo a quantidade de jogadores

game_players = None

while True:
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

    if _count == '1' or _count == '2' or _count == '3':
        game_players = int(_count)

        time.sleep(2)
        break
    else:
        print("\n  Você inseriu um valor inválido, verifique e tente novamente.")

    time.sleep(2)

# Escolhendo os personagens

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

while _index != game_players:
    os.system("cls")

    _index += 1

    print(f"           ___________________________________{globals()[f"ASCII_NUMBER_{_index}_PART_1"]}____ ")
    print(f"  ________|    ____  _                        {globals()[f"ASCII_NUMBER_{_index}_PART_2"]}   |________")
    print(f"  \\       |   |  _ \\| | __ _ _   _  ___ _ __  {globals()[f"ASCII_NUMBER_{_index}_PART_3"]}   |       /")
    print(f"   \\      |   | |_) | |/ _` | | | |/ _ \\ '__| {globals()[f"ASCII_NUMBER_{_index}_PART_4"]}   |      /")
    print(f"    \\     |   |  __/| | (_| | |_| |  __/ |    {globals()[f"ASCII_NUMBER_{_index}_PART_5"]}   |     /")
    print(f"    /     |   |_|   |_|\\__,_|\\__, |\\___|_|    {globals()[f"ASCII_NUMBER_{_index}_PART_6"]}   |     \\")
    print(f"   /      |_________________ |___/ ___________{globals()[f"ASCII_NUMBER_{_index}_PART_7"]}___|      \\")
    print(f"  /__________)                                {globals()[f"ASCII_NUMBER_{_index}_PART_8"]}(__________\\")
    print()
    print(f"    Você deve escolher o nome do seu personagem. Certifique-se")
    print(f"  de ser maior que 3 e menor que 6 caracteres.")
    print()

    _name = input("  >> ")

    if (len(_name) > 2) and (len(_name) < 7):
        globals()[f"player_display_{_index}"] = _name

        # TODO: adicionar seleção de equipamento
    else:
        print("\n  O nome fornecido não respeita as regras estabelecidas.")
        _index -= 1

    time.sleep(2)

#
# PARTIDA
#

game_player = game_players
game_winner = -1
game_deaths = 0

while game_deaths != game_players and game_winner == -1:
    # Changing player

    if game_player == game_players:
        game_player = 1
    else:
        game_player += 1

    # Verifying health

    if globals()[f'player_health_{game_player}'] == 0:
        continue

    # Weapon's properties

    while True:
        os.system("cls")

        print("           ___________________________________________________________________ ")
        print("  ________|       _    ____  __  __    _    __  __ _____ _   _ _____ ___     |________")
        print("  \\       |      / \\  |  _ \\|  \\/  |  / \\  |  \\/  | ____| \\ | |_   _/ _ \\    |       /")
        print("   \\      |     / _ \\ | |_) | |\\/| | / _ \\ | |\\/| |  _| |  \\| | | || | | |   |      /")
        print("    \\     |    / ___ \\|  _ <| |  | |/ ___ \\| |  | | |___| |\\  | | || |_| |   |     /")
        print("    /     |   /_/   \\_\\_| \\_\\_|  |_/_/   \\_\\_|  |_|_____|_| \\_| |_| \\___/    |     \\")
        print("   /      |__________________________________________________________________|      \\")
        print("  /__________)                                                            (__________\\")
        print()
        print("    Escolha o armamento que você deseja para o jogo. Certifique-se de usar ")
        print("  o valor correspondente ao desejado.")
        print()

        _index = 1

        while f"WEAPON_DISPLAY_{_index}" in globals():
            print(f"    {_index}:")
            print(f"      - Título: {globals()[f"WEAPON_DISPLAY_{_index}"]}")
            print(f"      - Precisão: {globals()[f"WEAPON_PRECISION_{_index}"]}")
            print(f"      - Dano: {globals()[f"WEAPON_DAMAGE_{_index}"]}")
            print(f"      - Velocidade: {globals()[f"WEAPON_SPEED_{_index}"]}")
            print()

            _index += 1

        _weapon = input("  >> ")

        if f"WEAPON_DISPLAY_{_weapon}" in globals():
            round_weapon_display = globals()[f"WEAPON_DISPLAY_{_weapon}"]
            round_weapon_precision = globals()[f"WEAPON_PRECISION_{_weapon}"]
            round_weapon_damage = globals()[f"WEAPON_DAMAGE_{_weapon}"]
            round_weapon_speed = globals()[f"WEAPON_SPEED_{_weapon}"]

            print(f"\n  O armamento {round_weapon_display} foi escolhido com sucesso!")

            time.sleep(2)
            break
        else:
            print("\n  Você inseriu um valor inválido, verifique e tente novamente.")

        time.sleep(2)

    # Target's properties

    round_target_speed = random.uniform(
        difficulty_speed - (difficulty_speed * 0.3), difficulty_speed + (difficulty_speed * 0.3)
    )
    round_target_path = False

    round_target_x = 55
    round_target_y = 1

    # Trail's properties

    round_trail_speed = random.uniform(
        round_weapon_speed - (round_weapon_speed * 0.3), round_weapon_speed + (round_weapon_speed * 0.3)
    )
    round_trail_path = True

    round_trail_head_x = 7
    round_trail_head_y = 5

    round_trail_tail_x = 6
    round_trail_tail_y = 5

    # Other's properties

    round_running = True
    round_time = 0
    round_won = random.random() < (round_weapon_precision / 100)

    # Target prediction

    round_target_x_final = round_target_x
    round_target_y_final = round_target_y

    _fake_time = 0
    _fake_final = (round_trail_speed * 48) * 1000
    _fake_path = 0

    while _fake_time <= _fake_final:
        if _fake_path:
            round_target_y_final += 1
        else:
            round_target_y_final -= 1

        if round_target_y_final == 5:
            _fake_path = 0
        elif round_target_y_final == 0:
            _fake_path = 1

        _fake_time += (round_target_speed * 1000)

    # Trail prediction

    if round_won:
        round_trail_x_final = round_target_x
        round_trail_y_final = round_target_y + 3
    else:
        round_trail_x_final = random.randint(40, 54)
        round_trail_y_final = 0

    #
    # Let's play
    #

    next_trail_update = 0
    next_target_update = 0

    while round_running:
        screen_updated = next_target_update <= round_time or next_trail_update <= round_time

        # Updating target

        if next_target_update <= round_time:
            if round_target_path:
                round_target_y += 1
            else:
                round_target_y -= 1

            if round_target_y == 5:
                round_target_path = False
            elif round_target_y == 0:
                round_target_path = True

            next_target_update = round_time + (round_target_speed * 1000)

        # Updating trail

        if next_trail_update <= round_time:
            round_trail_tail_x = round_trail_head_x
            round_trail_tail_y = round_trail_head_y

            if round_trail_head_x != round_trail_x_final:
                round_trail_head_x += 1

            if round_trail_head_y != round_trail_y_final:
                if round_trail_path:
                    if random.randint(0, 3) == 1:
                        round_trail_head_y += 1

                    if round_trail_head_y == 8:
                        round_trail_path = False
                elif (round_trail_x_final - round_trail_head_x) > round_trail_head_y:
                    if random.randint(0, 3) == 1:
                        round_trail_head_y -= 1
                else:
                    round_trail_head_y -= 1

            next_trail_update = round_time + (round_trail_speed * 1000)

        # Updating screen

        if screen_updated:
            os.system('cls')

            # Target

            screen_target_part_1 = "     "
            screen_target_part_2 = "     "
            screen_target_part_3 = "     "
            screen_target_part_4 = "     "
            screen_target_part_5 = "     "
            screen_target_part_6 = "     "
            screen_target_part_7 = "     "
            screen_target_part_8 = "     "

            _index = round_target_y - 1

            while _index != -1:
                globals()[f"screen_target_part_{8 - _index}"] = ASCII_TARGET_PART_4
                _index -= 1

            globals()[f"screen_target_part_{8 - round_target_y - 2}"] = ASCII_TARGET_PART_1
            globals()[f"screen_target_part_{8 - round_target_y - 1}"] = ASCII_TARGET_PART_2
            globals()[f"screen_target_part_{8 - round_target_y}"] = ASCII_TARGET_PART_3

            # World

            screen_world_part_1 = "                                                                       "
            screen_world_part_2 = f"  O                                                  {screen_target_part_1}             "
            screen_world_part_3 = f" /|\\                                                 {screen_target_part_2}             "
            screen_world_part_4 = f" / \\                                                 {screen_target_part_3}             "
            screen_world_part_5 = f" ---                                                 {screen_target_part_4}            _"
            screen_world_part_6 = f"/__/|__                                              {screen_target_part_5}         __//|"
            screen_world_part_7 = f"|__|/_/|__                                           {screen_target_part_6}       _/_|_||"
            screen_world_part_8 = f"|_|___|/_/|__                                        {screen_target_part_7}    __/_|___||"
            screen_world_part_9 = f"|___|____|/_/|__                                     {screen_target_part_8} __/_|____|_||"

            _index = 0

            while _index != 9:
                x = 0
                y = _index

                current_line = globals()[f"screen_world_part_{9 - y}"]
                updated_line = ""

                while x != 71:
                    if (x == round_trail_head_x) and (y == round_trail_head_y):
                        updated_line += ASCII_TRAIL_PART_1
                    elif (x == round_trail_tail_x) and (y == round_trail_tail_y):
                        updated_line += ASCII_TRAIL_PART_2
                    else:
                        updated_line += current_line[x]
                    x += 1

                globals()[f"screen_world_part_{9 - y}"] = updated_line

                _index += 1

            # Player's data

            screen_player_display = globals()[f'player_display_{game_player}']

            if len(screen_player_display) != 6:
                screen_player_display = "      "[:(6 - len(screen_player_display))] + screen_player_display

            screen_player_health_num = globals()[f'player_health_{game_player}']
            screen_player_health_bar = "=============="[:(int(screen_player_health_num * 14 / 100))]

            # TODO: adicionar animação do colete

            if len(screen_player_health_bar) != 14:
                screen_player_health_bar = screen_player_health_bar + "              "[
                                                                      :(14 - len(screen_player_health_bar))]

            if len(str(screen_player_health_num)) != 3:
                screen_player_health_num = "   "[:(3 - len(str(screen_player_health_num)))] + str(
                    screen_player_health_num)

            # Target's data

            screen_target_health_num = globals()[f'player_target_{game_player}']
            screen_target_health_bar = "=============="[:(int(screen_target_health_num * 14 / 100))]

            if len(str(screen_target_health_num)) != 3:
                screen_target_health_num = str(screen_target_health_num) + "   "[
                                                                           :(3 - len(str(screen_target_health_num)))]

            if len(screen_target_health_bar) != 14:
                screen_target_health_bar = screen_target_health_bar + "              "[
                                                                      :(14 - len(screen_target_health_bar))]

            # Round time

            _screen_time_min = int(round_time / 60000)
            _screen_time_sec = int((round_time - _screen_time_min * 60000) / 1000)

            screen_time = "                                                                       "[:int(73 / 2 - 2.5)]
            screen_time += f"{_screen_time_min:02d}:{_screen_time_sec:02d}"

            # Drawing

            print("                __________________________________________")
            print("       ________|    ____            _   _     _          |________")
            print("       \\       |   |  _ \\ __ _ _ __| |_(_) __| | __ _    |       /")
            print("        \\      |   | |_) / _` | '__| __| |/ _` |/ _` |   |      /")
            print("         \\     |   |  __/ (_| | |  | |_| | (_| | (_| |   |     /")
            print("         /     |   |_|   \\__,_|_|   \\__|_|\\__,_|\\__,_|   |     \\")
            print("        /      |_________________________________________|      \\")
            print("       /__________)                                   (__________\\")
            print(screen_time)
            print(
                f"       {screen_player_display} [{screen_player_health_bar}] {screen_player_health_num} --- {screen_target_health_num} [{screen_target_health_bar}]   Alvo")
            print()
            print()
            print()
            print(screen_world_part_1)
            print(screen_world_part_2)
            print(screen_world_part_3)
            print(screen_world_part_4)
            print(screen_world_part_5)
            print(screen_world_part_6)
            print(screen_world_part_7)
            print(screen_world_part_8)
            print(screen_world_part_9)
            print("|_|___|_____|/_/|______________________________________|__/_|_____|___||")
            print("|___|___|__|___|/__/___/___/___/___/___/___/___/___/___/_|_____|____|_||")
            print("|_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___||")
            print("|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_||")
            print("|_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|/")

        # Health check

        round_running = round_trail_head_x != round_trail_x_final or round_trail_head_y != round_trail_y_final

        # Elapsed time

        round_time += 50

        time.sleep(0.05)

    # Damage

    if round_won:
        globals()[f'player_target_{game_player}'] = max(
            globals()[f'player_target_{game_player}'] - round_weapon_damage, 0)
    else:
        globals()[f'player_health_{game_player}'] = max(
            globals()[f'player_health_{game_player}'] - difficulty_damage, 0)

    # TODO: adicionar animação ao receber dano ou dar dano;

    # Winner

    if globals()[f'player_target_{game_player}'] == 0:
        game_winner = game_player

    # TODO: adicionar animação na vitória;

    # Loser

    if globals()[f'player_health_{game_player}'] == 0:
        game_deaths += 1

    # TODO: adicionar animação na perda;

    time.sleep(2)