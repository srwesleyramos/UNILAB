import os

ASCII_TARGET_LINE_1 = " .-. "
ASCII_TARGET_LINE_2 = ". o ."
ASCII_TARGET_LINE_3 = " ._. "
ASCII_TARGET_LINE_4 = "  |  "

ASCII_TRAIL_LINE_1 = "@"
ASCII_TRAIL_LINE_2 = "#"

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


def draw(round_target_y, round_trail_head_x, round_trail_head_y, round_trail_tail_x, round_trail_tail_y,
         difficulty_display, player_health, player_target):
    global ASCII_TARGET_LINE_1, ASCII_TARGET_LINE_2, ASCII_TARGET_LINE_3, ASCII_TARGET_LINE_4
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

    globals()[f"target_line_{8 - round_target_y - 2}"] = ASCII_TARGET_LINE_1
    globals()[f"target_line_{8 - round_target_y - 1}"] = ASCII_TARGET_LINE_2
    globals()[f"target_line_{8 - round_target_y}"] = ASCII_TARGET_LINE_3

    _index = round_target_y - 1

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

    while (_index != 9):
        x = 0
        y = _index

        current_line = globals()[f"line_{9 - y}"]
        updated_line = ""

        while (x != 71):
            if (x == round_trail_head_x) and (y == round_trail_head_y):
                updated_line += ASCII_TRAIL_LINE_1
            elif (x == round_trail_tail_x) and (y == round_trail_tail_y):
                updated_line += ASCII_TRAIL_LINE_2
            else:
                updated_line += current_line[x]
            x += 1

            globals()[f"line_{9 - y}"] = updated_line

        _index += 1

    ##
    ## Calculando player health's bar
    ##

    player_health_bar = ''
    player_health_tmp = player_health * 14 / 100

    #   14 = 100
    #   50 = y

    _player_health_index = 0

    while _player_health_index < 14:
        if _player_health_index < player_health_tmp:
            player_health_bar += '='
        else:
            player_health_bar += ' '

        _player_health_index += 1

    ##
    ## Calculando player health's bar
    ##

    player_target_bar = ''
    player_target_tmp = player_target * 14 / 100

    #   14 = 100
    #   50 = y

    _player_target_index = 0

    while _player_target_index < 14:
        if _player_target_index < player_target_tmp:
            player_target_bar += '='
        else:
            player_target_bar += ' '

        _player_target_index += 1

    ##
    ## Enviando na tela
    ##

    str_1 = ''
    str_1_i = 0

    while str_1_i < (3 - len(str(player_health))):
        str_1 += ' '
        str_1_i += 1

    str_2 = ''
    str_2_i = 0

    while str_2_i < (3 - len(str(player_target))):
        str_2 += ' '
        str_2_i += 1

    print("                __________________________________________")
    print("       ________|    ____            _   _     _          |________")
    print("       \\       |   |  _ \\ __ _ _ __| |_(_) __| | __ _    |       /")
    print("        \\      |   | |_) / _` | '__| __| |/ _` |/ _` |   |      /")
    print("         \\     |   |  __/ (_| | |  | |_| | (_| | (_| |   |     /")
    print("         /     |   |_|   \\__,_|_|   \\__|_|\\__,_|\\__,_|   |     \\")
    print("        /      |_________________________________________|      \\")
    print("       /__________)                                   (__________\\")
    print(difficulty_centered)
    print(
        f"       Wesley [{player_health_bar}] {str_1}{player_health} --- {player_target}{str_2} [{player_target_bar}]   Alvo")
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
