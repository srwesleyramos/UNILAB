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
DIFFICULTY_SPEED_2 = 5/2

DIFFICULTY_DISPLAY_3 = "Díficil"
DIFFICULTY_DAMAGE_3 = 30
DIFFICULTY_SPEED_3 = 5/4

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
## Funções de ambiente (DEV)
##

line_1 = ""
line_2 = ""
line_3 = ""
line_4 = ""
line_5 = ""
line_6 = ""
line_7 = ""
line_8 = ""
line_9 = ""

target_line_1 = "     "
target_line_2 = "     "
target_line_3 = "     "
target_line_4 = "     "
target_line_5 = "     "
target_line_6 = "     "
target_line_7 = "     "
target_line_8 = "     "

def draw():
    global ASCII_TARGET_LINE_1, ASCII_TARGET_LINE_2, ASCII_TARGET_LINE_3, ASCII_TARGET_LINE_4, target_x, target_y, difficulty_display
    global target_line_1, target_line_2, target_line_3, target_line_4, target_line_5, target_line_6, target_line_7, target_line_8
    global line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8, line_9

    os.system("cls")

    ##
    ## Atualizando o alvo
    ##

    target_line_1 = "     "
    target_line_2 = "     "
    target_line_3 = "     "
    target_line_4 = "     "
    target_line_5 = "     "
    target_line_6 = "     "
    target_line_7 = "     "
    target_line_8 = "     "

    globals()[f"target_line_{8 - target_y - 2}"] = ASCII_TARGET_LINE_1
    globals()[f"target_line_{8 - target_y - 1}"] = ASCII_TARGET_LINE_2
    globals()[f"target_line_{8 - target_y}"] = ASCII_TARGET_LINE_3

    _index = target_y - 1

    while (_index != -1):
        globals()[f"target_line_{8 - _index}"] = ASCII_TARGET_LINE_4
        _index -= 1

    ##
    ## Centralizando a dificuldade
    ##

    difficulty_centered = ""

    while (len(difficulty_centered) < (73 - len(difficulty_display)) / 2):
        difficulty_centered += " "
    
    difficulty_centered += difficulty_display

    ##
    ## Atualizando o rastro
    ##

    line_1 = "                                                                       "
    line_2 = f"  O                                                  {target_line_1}             "
    line_3 = f" /|\\                                                 {target_line_2}             "
    line_4 = f" / \\                                                 {target_line_3}             "
    line_5 = f" ---                                                 {target_line_4}            _"
    line_6 = f"/__/|__                                              {target_line_5}         __//|"
    line_7 = f"|__|/_/|__                                           {target_line_6}       _/_|_||"
    line_8 = f"|_|___|/_/|__                                        {target_line_7}    __/_|___||"
    line_9 = f"|___|____|/_/|__                                     {target_line_8} __/_|____|_||"

    _index = 0

    while (_index != 8):
        x = 0
        y = _index

        current_line = globals()[f"line_{9-y}"]
        updated_line = ""
        
        while (x != 71):
            if (x == trail_head_x) and (y == trail_head_y):
                updated_line += ASCII_TRAIL_LINE_1
            elif (x == trail_tail_x) and (y == trail_tail_y):
                updated_line += ASCII_TRAIL_LINE_2
            else:
                updated_line += current_line[x]
            x += 1
        
            globals()[f"line_{9-y}"] = updated_line
        
        _index += 1

    ##
    ## Enviando na tela
    ##

    print("                __________________________________________")
    print("       ________|    ____            _   _     _          |________")
    print("       \\       |   |  _ \\ __ _ _ __| |_(_) __| | __ _    |       /")
    print("        \\      |   | |_) / _` | '__| __| |/ _` |/ _` |   |      /")
    print("         \\     |   |  __/ (_| | |  | |_| | (_| | (_| |   |     /")
    print("         /     |   |_|   \\__,_|_|   \\__|_|\\__,_|\\__,_|   |     \\")
    print("        /      |_________________________________________|      \\")
    print("       /__________)                                   (__________\\")
    print(difficulty_centered)
    print("       Wesley [============  ] 233 --- 078 [=========     ]   Alvo")
    print("                                                                       ")
    print("                                                                       ")
    print("                                                                       ")
    print(line_1)    
    print(line_2)    
    print(line_3)    
    print(line_4)    
    print(line_5)    
    print(line_6)    
    print(line_7)    
    print(line_8)    
    print(line_9)    
    print("|_|___|_____|/_/|______________________________________|__/_|_____|___||")
    print("|___|___|__|___|/__/___/___/___/___/___/___/___/___/___/_|_____|____|_||")
    print("|_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___||")
    print("|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|_||")
    print("|_|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|/")

##
## Variaveis de ambiente (DEV)
##

difficulty_display = 'Médio'
difficulty_damage = 25
difficulty_speed = 0.33

players_count = 3

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

  trail_head_x = 7
  trail_head_y = 6
  trail_head_d = True

  trail_tail_x = 6
  trail_tail_y = 6

  target_x = 55
  target_y = 1
  target_s = random.uniform(
    difficulty_speed - (difficulty_speed * 0.3), difficulty_speed + (difficulty_speed * 0.3)
  )
  target_d = False

  weapon_display = 'Arco e flecha'
  weapon_precision = 80
  weapon_damage = 20

  ##
  ## Calculando TARGET
  ##

  final_target_x = target_x
  final_target_y = target_y

  _time = 0
  _state = 0

  while (_time <= 5000):
    if (_state):
      final_target_y += 1
    else:
      final_target_y -= 1

    if (final_target_y == 5):
      _state = 0
    elif (final_target_y == 0):
      _state = 1
    
    _time += (target_s * 1000)

  ##
  ## Calculando TRAIL
  ##

  if ((weapon_precision / 10) > random.randrange(1, 10)):
    final_trail_x = final_target_x
    final_trail_y = final_target_y + 2
  else:
    final_trail_x = 73

    while (True):
      final_trail_y = random.randrange(0, 8)

      if (final_trail_y >= (final_target_y + 1) and final_trail_y <= (final_target_y + 3)):
        continue
      else:
        break

  ##
  ## Let's play baby!
  ##

  game_time = 0

  next_trail_update = 0
  next_target_update = 0

  while (game_time <= 5000):
    if (next_target_update <= game_time):
        if (target_d):
            target_y += 1
        else:
            target_y -= 1

        if (target_y == 5):
            target_d = False
        elif (target_y == 0):
            target_d = True
        
        next_target_update = game_time + (target_s * 1000)
    
    if (next_trail_update <= game_time):
      trail_tail_x = trail_head_x
      trail_tail_y = trail_head_y

      trail_head_x += 1

      if (trail_head_d):
        if (trail_head_y < 7):
          if (random.randint(0, 6) == 1):
            trail_head_y += 1
        else:
          trail_head_d = False
          if (random.randint(0, 6) == 1):
            trail_head_y -= 1
      else:
        if (random.randint(0, 6) == 1):
          trail_head_y -= 1

    draw()

    game_time += (5 / 55) * 1000
    time.sleep((5 / 55))
  break
