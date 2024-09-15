#
#             _____ _                                 _            
#            |_   _(_)_ __ ___     __ _  ___     __ _| |_   _____  
#              | | | | '__/ _ \   / _` |/ _ \   / _` | \ \ / / _ \ 
#              | | | | | | (_) | | (_| | (_) | | (_| | |\ V / (_) |
#              |_| |_|_|  \___/   \__,_|\___/   \__,_|_| \_/ \___/ 
#           
#                              by @srwesleyramos
#

import os
import random
import time

from paint import draw

# 
# CONFIGURAÇÕES
#

##
## Armamento
##

WEAPON_DISPLAY_1 = "Arco e Flecha"
WEAPON_PRECISION_1 = 80
WEAPON_DAMAGE_1 = 20

WEAPON_DISPLAY_2 = "Pistola"
WEAPON_PRECISION_2 = 40
WEAPON_DAMAGE_2 = 60

WEAPON_DISPLAY_3 = "Bazuka"
WEAPON_PRECISION_3 = 10
WEAPON_DAMAGE_3 = 80

##
## Dificuldade
##

DIFFICULTY_DISPLAY_1 = "Fácil"
DIFFICULTY_DAMAGE_1 = 20
DIFFICULTY_SPEED_1 = 0.0

DIFFICULTY_DISPLAY_2 = "Médio"
DIFFICULTY_DAMAGE_2 = 25
DIFFICULTY_SPEED_2 = 5 / 2

DIFFICULTY_DISPLAY_3 = "Díficil"
DIFFICULTY_DAMAGE_3 = 30
DIFFICULTY_SPEED_3 = 5 / 4

##
## Decoração
##

ASCII_NUMBER_1_LINE_1 = "___"
ASCII_NUMBER_1_LINE_2 = " _ "
ASCII_NUMBER_1_LINE_3 = "/ |"
ASCII_NUMBER_1_LINE_4 = "| |"
ASCII_NUMBER_1_LINE_5 = "| |"
ASCII_NUMBER_1_LINE_6 = "|_|"
ASCII_NUMBER_1_LINE_7 = "___"
ASCII_NUMBER_1_LINE_8 = "   "

ASCII_NUMBER_2_LINE_1 = "_______"
ASCII_NUMBER_2_LINE_2 = " ____  "
ASCII_NUMBER_2_LINE_3 = "|___ \\ "
ASCII_NUMBER_2_LINE_4 = "  __) |"
ASCII_NUMBER_2_LINE_5 = " / __/ "
ASCII_NUMBER_2_LINE_6 = "|_____|"
ASCII_NUMBER_2_LINE_7 = "_______"
ASCII_NUMBER_2_LINE_8 = "       "

ASCII_NUMBER_3_LINE_1 = "_______"
ASCII_NUMBER_3_LINE_2 = " _____ "
ASCII_NUMBER_3_LINE_3 = "|___ / "
ASCII_NUMBER_3_LINE_4 = "  |_ \\ "
ASCII_NUMBER_3_LINE_5 = " ___) |"
ASCII_NUMBER_3_LINE_6 = "|____/ "
ASCII_NUMBER_3_LINE_7 = "_______"
ASCII_NUMBER_3_LINE_8 = "       "

ASCII_TARGET_LINE_1 = " .-. "
ASCII_TARGET_LINE_2 = ". o ."
ASCII_TARGET_LINE_3 = " ._. "
ASCII_TARGET_LINE_4 = "  |  "

ASCII_TRAIL_LINE_1 = "@"
ASCII_TRAIL_LINE_2 = "#"

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

##
## Variaveis de ambiente (DEV)
##

difficulty_display = 'Médio'
difficulty_damage = 25
difficulty_speed = 0.33

game_players = 3

player_display_1 = 'Wesley'
player_health_1 = 100
player_target_1 = 200

player_display_2 = "Sid"
player_health_2 = 100
player_target_2 = 200

player_display_3 = 'Joao'
player_health_3 = 100
player_target_3 = 200

##
## Iniciando a partida
##

game_player = 1
game_running = True

while (game_running):
    ##
    ## Propriedades do round
    ##

    ### WEAPON

    round_weapon_display = 'Arco e flecha'
    round_weapon_precision = 80
    round_weapon_damage = 20
    round_weapon_speed = 0.35

    ### TARGET

    round_target_speed = random.uniform(
        difficulty_speed - (difficulty_speed * 0.3), difficulty_speed + (difficulty_speed * 0.3)
    )
    round_target_path = False

    round_target_x = 55
    round_target_y = 1

    ### TRAIL

    round_trail_speed = random.uniform(
        round_weapon_speed - (round_weapon_speed * 0.3), round_weapon_speed + (round_weapon_speed * 0.3)
    )
    round_trail_path = True

    round_trail_head_x = 7
    round_trail_head_y = 6

    round_trail_tail_x = 6
    round_trail_tail_y = 6

    ### OTHERS

    round_running = True
    round_time = 0
    round_win = (round_weapon_precision / 100) < random.random()

    ##
    ## Cálculos
    ##

    ### Calculando a posição final do alvo

    round_final_target_x = round_target_x
    round_final_target_y = round_target_y

    _time = 0
    _time_final = (round_weapon_speed * 1000) * 48
    _path = 0

    while (_time <= _time_final):
        if (_path):
            round_final_target_y += 1
        else:
            round_final_target_y -= 1

        if (round_final_target_y == 5):
            _path = 0
        elif (round_final_target_y == 0):
            _path = 1

        _time += (round_target_speed * 1000)
    
    ### Calculando a posição final da munição

    if (round_win):
        round_final_trail_x = round_target_x
        round_final_trail_y = round_target_y
    else:
        round_final_trail_x = random.randint(40, 54)
        round_final_trail_y = 0
    
    ##
    ## Let's play
    ##

    next_trail_update = 0
    next_target_update = 0

    while (round_running):
        ### Updating target

        if (next_target_update <= round_time):
            if (round_target_path):
                round_target_y += 1
            else:
                round_target_y -= 1

            if (round_target_y == 5):
                round_target_path = False
            elif (round_target_y == 0):
                round_target_path = True

            next_target_update = round_time + (round_target_speed * 1000)