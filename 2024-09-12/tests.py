#
# HEADER
#

import os
import time

#
# PRODUÇÃO
#

ASCII_TARGET_LINE_1 = " .-. "
ASCII_TARGET_LINE_2 = ". o ."
ASCII_TARGET_LINE_3 = " ._. "
ASCII_TARGET_LINE_4 = "  |  "

trail_head_ascii = '.'
trail_head_x = 7
trail_head_y = 6

trail_tail_ascii = '.'
trail_tail_x = 6
trail_tail_y = 6

target_y = 0

#
# FACILITANDO O DEBUG
#

target_line_1 = "     "
target_line_2 = "     "
target_line_3 = "     "
target_line_4 = "     "
target_line_5 = "     "
target_line_6 = "     "
target_line_7 = "     "
target_line_8 = "     "

_state = True

def updateTarget():
    global target_y, _state

    if (target_y == 5):
        _state = False
    elif (target_y == 0):
        _state = True

    if (_state):
        target_y += 1
    else:
        target_y -= 1

line_1 = ""
line_2 = ""
line_3 = ""
line_4 = ""
line_5 = ""
line_6 = ""
line_7 = ""
line_8 = ""
line_9 = ""

def drawTrail():
    global trail_head_x, trail_tail_x, line_1, line_2, line_3, line_4, line_5, line_6, line_7, line_8, line_9

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
                updated_line += trail_head_ascii
            elif (x == trail_tail_x) and (y == trail_tail_y):
                updated_line += trail_head_ascii
            else:
                updated_line += current_line[x]
            x += 1
        
            globals()[f"line_{9-y}"] = updated_line
        
        _index += 1
    
    time.sleep(0.001)

    trail_head_x += 1
    trail_tail_x += 1

def updateTrail():
    drawTrail()

#
# PRODUÇÃO
#

while (True):
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
    ## Atualizando o rastro
    ##

    print("                __________________________________________")
    print("       ________|    ____            _   _     _          |________")
    print("       \\       |   |  _ \\ __ _ _ __| |_(_) __| | __ _    |       /")
    print("        \\      |   | |_) / _` | '__| __| |/ _` |/ _` |   |      /")
    print("         \\     |   |  __/ (_| | |  | |_| | (_| | (_| |   |     /")
    print("         /     |   |_|   \\__,_|_|   \\__|_|\\__,_|\\__,_|   |     \\")
    print("        /      |_________________________________________|      \\")
    print("       /__________)                                   (__________\\")
    print("       /__________)               Fácil                (__________\\")
    print()
    print("       Wesley [============   ] 233 --- 078 [=========      ] Alvo")
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

    updateTarget()
    updateTrail()

    os.system("cls")
