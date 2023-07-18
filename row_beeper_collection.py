from stanfordkarel import *

def main():
    collect_beepers_all_rows()

def collect_beepers_this_row():
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        move()
    if beepers_present():
        pick_beeper()

def move_to_next_row_on_right_end():
    turn_left()
    if front_is_clear():
        move()
        turn_left()

def move_to_next_row_on_left_end():
    turn_right()
    if front_is_clear():
        move()
        turn_right()

def collect_beepers_all_rows():
    left = False
    while front_is_clear():
        collect_beepers_this_row()
        if left is True:
            move_to_next_row_on_left_end()
            left = False
        else:
            move_to_next_row_on_right_end()
            left = True
    collect_beepers_this_row()
  
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

if __name__ == "__main__":
    run_karel_program("sample_quad1")