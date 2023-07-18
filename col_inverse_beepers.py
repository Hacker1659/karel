from stanfordkarel import *

def main():
    collect_beepers_in_all_columns() 
    go_back()

def turn_right():
    turn_left()
    turn_left()

def turn_around():
    turn_left()
    turn_left()

def inverse_beeper():
    if beepers_present():
        pick_beeper()
    else:
        put_beeper() 

def collect_beepers_in_column():
    turn_left()
    while front_is_clear():
        inverse_beeper()    
        move()
    inverse_beeper()
    turn_right()
    while front_is_clear():
        move()
    turn_left()

def collect_beepers_in_all_columns():
    while front_is_clear():
        collect_beepers_in_column()
        move()
    collect_beepers_in_column()

def go_back():
    turn_around()
    while front_is_clear():
        move()
    turn_around()

if __name__ == "__main__":
    run_karel_program("sample_quad1")