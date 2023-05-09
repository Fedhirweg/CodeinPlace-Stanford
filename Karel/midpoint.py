from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    #Fill the street with beepers
    while front_is_clear():
        move()
        put_beeper()
    """
    Return to start of the world, otherwise for some reason i can't seem to get
    to the left side of the middle on even streets consistently.
    """
    
    turn_around()
    pick_beeper()
    while front_is_clear():
        move()
    turn_around()
    move()

    #Try to find middle while collecting beepers at the edges
    
    while beepers_present():
        if front_is_clear():
            move()
        if no_beepers_present():
            turn_around()
            move()
            pick_beeper()
            move()
    #trying to return to middle on even and odd long worlds
    if facing_east():   #for even worlds
        turn_around()
        move()
        turn_around()
        put_beeper()
    else:               #for odd worlds
        turn_around()
        move()
        put_beeper()
        
def turn_around():
    turn_left()
    turn_left()
    
if __name__ == '__main__':
    main()
