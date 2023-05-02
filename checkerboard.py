from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():
    if front_is_blocked():
        turn_left()
        while front_is_clear():
            put_beeper()
            if front_is_clear():
                move()
            if front_is_clear():
                move()
                if front_is_blocked():
                    put_beeper()
        turn_around()
        turn_back()
        turn_left()
        
        
    else:
        while front_is_clear():
            fill_odd_row()
        turn_left()
        turn_back()
        turn_around()
        move()
        turn_right()
        while front_is_clear():
            fill_even_row()
        turn_left()
        turn_back()
        turn_left()
    
    
def fill_odd_row():
    while front_is_clear():
        put_beeper()
        if front_is_clear():
            move()
        if front_is_clear():
            move()
            if front_is_blocked():
                put_beeper()
    turn_left()
    if front_is_blocked():
        turn_left()
        while front_is_clear():
            move()
    else:
        turn_left()
        while front_is_clear():
            move()
        turn_right()
        move()
        if front_is_clear():
            move()
            turn_right()
        else:
            turn_left()
            
def fill_even_row():
    while front_is_clear():
        if front_is_clear():
            move()
        put_beeper()
        if front_is_clear():
            move()
    turn_left()
    if front_is_blocked():
        turn_left()
        turn_back()
    else:
        turn_left()
        while front_is_clear():
            move()
        turn_right()
        move()
        if front_is_clear():
            move()
            turn_right()
        else:
            turn_left()
            
def turn_back():
    while front_is_clear():
        move()
    
def turn_right():
    for i in range (3):
        turn_left()

def turn_around():
    turn_left()
    turn_left()

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
