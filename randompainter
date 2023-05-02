from karel.stanfordkarel import *

"""
Karel should paint the whole world, any color you want. 
As an extension, have karel randomly paint each corner.
"""


def main():
    while front_is_clear():
        fill_row()
    
    
def fill_row():
    while front_is_clear():
        if random():
            paint_corner("white")
        else:
            paint_corner("red")
        move()
    if random():
        paint_corner("white")
    else:
        paint_corner("red")
    #return if not last column
    turn_left()
    if front_is_blocked():
        turn_right()
    else:
        turn_left()
        while front_is_clear():
            move()
        turn_right()
        move()
        turn_right()
        
def turn_right():
    for i in range (3):
        turn_left()
        
# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
