import os
import random
import time

#
# CONFIGURAÇÕES
#

# Armas

WEAPON_DISPLAY_1 = "Arco e Flecha"
WEAPON_PRECISION_1 = 80
WEAPON_DAMAGE_1 = 20

WEAPON_DISPLAY_2 = "Pistola"
WEAPON_PRECISION_2 = 40
WEAPON_DAMAGE_2 = 60

WEAPON_DISPLAY_3 = "Bazuka"
WEAPON_PRECISION_3 = 10
WEAPON_DAMAGE_3 = 80

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

#
# ASCII TEXT
#

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

ASCII_TARGET_PART_1 = " .-. "
ASCII_TARGET_PART_2 = ". o ."
ASCII_TARGET_PART_3 = " ._. "
ASCII_TARGET_PART_4 = "  |  "

ASCII_TRAIL_PART_1 = "@"
ASCII_TRAIL_PART_2 = "#"

#
# APLICAÇÃO
#

print("     _____ _                                 _")
print("    |_   _(_)_ __ ___     __ _  ___     __ _| |_   _____")
print("      | | | | '__/ _ \\   / _` |/ _ \\   / _` | \\ \\ / / _ \\")
print("      | | | | | | (_) | | (_| | (_) | | (_| | |\\ V / (_) |")
print("      |_| |_|_|  \\___/   \\__,_|\\___/   \\__,_|_| \\_/ \\___/")
print()
print("                        by @srwesleyramos")
print()
print("          Bem-vindo(a) ao nosso jogo de tiro ao alvo!")
print()

#
# Variaveis de ambiente (DEV)
#

difficulty_display = 'Médio'
difficulty_damage = 25
difficulty_speed = 0.5

game_players = 1

player_display_1 = 'Wesley'
player_health_1 = 100
player_target_1 = 200

player_display_2 = "Sid"
player_health_2 = 100
player_target_2 = 200

player_display_3 = 'Joao'
player_health_3 = 100
player_target_3 = 200

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

    # TODO: Weapon's properties

    round_weapon_display = 'Arco e flecha'
    round_weapon_precision = 80
    round_weapon_damage = 20
    round_weapon_speed = 0.35

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
    round_won = (round_weapon_precision / 100) < random.random()

    # Target prediction

    round_target_x_final = round_target_x
    round_target_y_final = round_target_y

    _round_time = 0
    _round_final = (round_target_speed * 1000) * 48
    _round_path = 0

    while _round_time <= _round_final:
        if _round_path:
            round_target_y_final += 1
        else:
            round_target_y_final -= 1

        if round_target_y_final == 5:
            _round_path = 0
        elif round_target_y_final == 0:
            _round_path = 1

        _round_time += (round_target_speed * 1000)

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

            _target_part_1 = "     "
            _target_part_2 = "     "
            _target_part_3 = "     "
            _target_part_4 = "     "
            _target_part_5 = "     "
            _target_part_6 = "     "
            _target_part_7 = "     "
            _target_part_8 = "     "

            _index = round_target_y - 1

            while _index != -1:
                globals()[f"_target_part_{8 - _index}"] = ASCII_TARGET_PART_4
                _index -= 1

            globals()[f"_target_part_{8 - round_target_y - 2}"] = ASCII_TARGET_PART_1
            globals()[f"_target_part_{8 - round_target_y - 1}"] = ASCII_TARGET_PART_2
            globals()[f"_target_part_{8 - round_target_y}"] = ASCII_TARGET_PART_3

            # World

            _world_part_1 = "                                                                       "
            _world_part_2 = f"  O                                                  {_target_part_1}             "
            _world_part_3 = f" /|\\                                                 {_target_part_2}             "
            _world_part_4 = f" / \\                                                 {_target_part_3}             "
            _world_part_5 = f" ---                                                 {_target_part_4}            _"
            _world_part_6 = f"/__/|__                                              {_target_part_5}         __//|"
            _world_part_7 = f"|__|/_/|__                                           {_target_part_6}       _/_|_||"
            _world_part_8 = f"|_|___|/_/|__                                        {_target_part_7}    __/_|___||"
            _world_part_9 = f"|___|____|/_/|__                                     {_target_part_8} __/_|____|_||"

            _index = 0

            while _index != 9:
                x = 0
                y = _index

                current_line = globals()[f"_world_part_{9 - y}"]
                updated_line = ""

                while x != 71:
                    if (x == round_trail_head_x) and (y == round_trail_head_y):
                        updated_line += ASCII_TRAIL_PART_1
                    elif (x == round_trail_tail_x) and (y == round_trail_tail_y):
                        updated_line += ASCII_TRAIL_PART_2
                    else:
                        updated_line += current_line[x]
                    x += 1

                globals()[f"_world_part_{9 - y}"] = updated_line

                _index += 1

            # Player's data

            _player_display = globals()[f'player_display_{game_player}']

            if len(_player_display) != 6:
                _player_display = "      "[:(6 - len(_player_display))] + _player_display

            _player_health_num = globals()[f'player_health_{game_player}']
            _player_health_bar = "=============="[:(int(_player_health_num * 14 / 100))]

            if len(_player_health_bar) != 14:
                _player_health_bar = _player_health_bar + "              "[:(14 - len(_player_health_bar))]

            if len(str(_player_health_num)) != 3:
                _player_health_num = "   "[:(3 - len(str(_player_health_num)))] + str(_player_health_num)

            # Target's data

            _target_health_num = globals()[f'player_target_{game_player}']
            _target_health_bar = "=============="[:(int(_target_health_num * 14 / 100))]

            if len(_target_health_bar) != 14:
                _target_health_bar = _target_health_bar + "              "[:(14 - len(_target_health_bar))]

            if len(str(_target_health_num)) != 3:
                _target_health_num = str(_target_health_num) + "   "[:(3 - len(str(_target_health_num)))]

            # Drawing

            _difficulty = "                                                                       "[
                          :int(73 / 2 - len(difficulty_display) / 2)]
            _difficulty += difficulty_display

            print("                __________________________________________")
            print("       ________|    ____            _   _     _          |________")
            print("       \\       |   |  _ \\ __ _ _ __| |_(_) __| | __ _    |       /")
            print("        \\      |   | |_) / _` | '__| __| |/ _` |/ _` |   |      /")
            print("         \\     |   |  __/ (_| | |  | |_| | (_| | (_| |   |     /")
            print("         /     |   |_|   \\__,_|_|   \\__|_|\\__,_|\\__,_|   |     \\")
            print("        /      |_________________________________________|      \\")
            print("       /__________)                                   (__________\\")
            print(_difficulty)
            print(
                f"       {_player_display} [{_player_health_bar}] {_player_health_num} --- {_target_health_num} [{_target_health_bar}]   Alvo")
            print()
            print()
            print()
            print(_world_part_1)
            print(_world_part_2)
            print(_world_part_3)
            print(_world_part_4)
            print(_world_part_5)
            print(_world_part_6)
            print(_world_part_7)
            print(_world_part_8)
            print(_world_part_9)
            print("|_|___|_____|/_/|______________________________________|__/_|_____|___||")
            print("|___|___|__|___|/__/___/___/___/___/___/___/___/___/___/_|_____|____|_||")
            print("|_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___||")
            print("|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_||")
            print("|_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|/")

        # Health check

        round_running = round_trail_head_x != round_trail_x_final or round_trail_head_y != round_trail_y_final
        round_time += 50

        # Elapsed time

        time.sleep(0.05)

    # Damage

    if round_won:
        globals()[f'player_target_{game_player}'] = max(
            globals()[f'player_target_{game_player}'] - round_weapon_damage, 0)
    else:
        globals()[f'player_health_{game_player}'] = max(
            globals()[f'player_health_{game_player}'] - difficulty_damage, 0)

    # Winner

    if globals()[f'player_target_{game_player}'] == 0:
        game_winner = game_player

    # Loser

    if globals()[f'player_health_{game_player}'] == 0:
        game_deaths += 1
