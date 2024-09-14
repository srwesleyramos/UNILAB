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
DIFFICULTY_SPEED_2 = 1.5

DIFFICULTY_DISPLAY_3 = "Díficil"
DIFFICULTY_DAMAGE_3 = 30
DIFFICULTY_SPEED_3 = 2.0

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

ASCII_TRAIL_LINE_1 = "."
ASCII_TRAIL_LINE_2 = "."

#
# APLICAÇÃO
#

print("""
     _____ _                                 _            
    |_   _(_)_ __ ___     __ _  ___     __ _| |_   _____  
      | | | | '__/ _ \\   / _` |/ _ \\   / _` | \\ \\ / / _ \\ 
      | | | | | | (_) | | (_| | (_) | | (_| | |\\ V / (_) |
      |_| |_|_|  \\___/   \\__,_|\\___/   \\__,_|_| \\_/ \\___/ 

                        by @srwesleyramos

          Bem-vindo(a) ao nosso jogo de tiro ao alvo!
""")

##
## Variaveis de ambiente (DEV)
##

difficulty_display = ''
difficulty_damage = ''
difficulty_speed = ''

players_count = None

player_display_1 = None
player_health_1 = 100
player_target_1 = None

player_display_2 = None
player_health_2 = 100
player_target_2 = None

player_display_3 = None
player_health_3 = 100
player_target_3 = None

##
## Iniciando a partida
##

current_player = 1
# target_health = random.randint(100)

while (True):
    time.sleep(2)
    os.system("cls")

    print("                __________________________________________")
    print("       ________|    ____            _   _     _          |________")
    print("       \\       |   |  _ \\ __ _ _ __| |_(_) __| | __ _    |       /")
    print("        \\      |   | |_) / _` | '__| __| |/ _` |/ _` |   |      /")
    print("         \\     |   |  __/ (_| | |  | |_| | (_| | (_| |   |     /")
    print("         /     |   |_|   \\__,_|_|   \\__|_|\\__,_|\\__,_|   |     \\")
    print("        /      |_________________________________________|      \\")
    print("       /__________)                                   (__________\\")
    print()
