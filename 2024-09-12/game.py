#
#             _____ _                                 _
#            |_   _(_)_ __ ___     __ _  ___     __ _| |_   _____
#              | | | | '__/ _ \   / _` |/ _ \   / _` | \ \ / / _ \
#              | | | | | | (_) | | (_| | (_) | | (_| | |\ V / (_) |
#              |_| |_|_|  \___/   \__,_|\___/   \__,_|_| \_/ \___/
#
#                              by @srwesleyramos
#

import random
import time

import paint

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
game_running = True
game_winner = -1

while game_winner == -1:
    _game_player = 1
    _game_dead = 0

    while _game_player <= game_players:
        if globals()[f'player_health_{game_player}'] == 0:
            _game_dead += 1
        _game_player += 1

    if _game_dead == game_players:
        break

    if globals()[f'player_health_{game_player}'] != 0:
        if game_player == game_players:
            game_player = 1
        else:
            game_player += 1
    else:
        continue

    #
    # PROPRIEDADES - WEAPON
    #

    round_weapon_display = 'Arco e flecha'
    round_weapon_precision = 80
    round_weapon_damage = 20
    round_weapon_speed = 0.35

    #
    # PROPRIEDADES - TARGET
    #

    round_target_speed = random.uniform(
        difficulty_speed - (difficulty_speed * 0.3), difficulty_speed + (difficulty_speed * 0.3)
    )
    round_target_path = False

    round_target_x = 55
    round_target_y = 1

    #
    # PROPRIEDADES - TRAIL
    #

    round_trail_speed = random.uniform(
        round_weapon_speed - (round_weapon_speed * 0.3), round_weapon_speed + (round_weapon_speed * 0.3)
    )
    round_trail_path = True

    round_trail_head_x = 7
    round_trail_head_y = 5

    round_trail_tail_x = 6
    round_trail_tail_y = 5

    #
    # PROPRIEDADES - OTHERS
    #

    round_running = True
    round_time = 0
    round_won = (round_weapon_precision / 100) < random.random()

    #
    # TARGET
    #

    round_target_x_final = round_target_x
    round_target_y_final = round_target_y

    _round_time = 0
    _round_final = (round_weapon_speed * 1000) * 48
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

    #
    # TRAIL
    #

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

        # Drawing

        if screen_updated:
            paint.draw(round_target_y, round_trail_head_x, round_trail_head_y, round_trail_tail_x, round_trail_tail_y,
                       difficulty_display, globals()[f'player_health_{game_player}'], globals()[f'player_target_{game_player}'])

        round_running = round_trail_head_x != round_trail_x_final or round_trail_head_y != round_trail_y_final
        round_time += 5000

        # Elapsed time

        time.sleep(0.05)

    # Winner

    if round_won:
        globals()[f'player_target_{game_player}'] = max(
            globals()[f'player_target_{game_player}'] - round_weapon_damage, 0)
    else:
        globals()[f'player_health_{game_player}'] = max(
            globals()[f'player_health_{game_player}'] - difficulty_damage, 0)

    if globals()[f'player_target_{game_player}'] == 0:
        game_winner = game_player
