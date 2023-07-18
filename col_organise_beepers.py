from stanfordkarel import *

def main():
    collect_beepers_in_all_columns()
    go_back()

def turn_around():
    turn_left()
    turn_left()

def put_collected_beepers(beeper_count):
    for i in range(beeper_count):
        put_beeper()

def collect_beepers_in_this_column():
    turn_left()
    beeper_count = 0
    while front_is_clear():
        if beepers_present():
           pick_beeper()
           beeper_count = beeper_count + 1
        move()
    if beepers_present():
        pick_beeper()
        beeper_count = beeper_count + 1
    turn_around()     
    while front_is_clear():    
        move()
    turn_left()
    return beeper_count

def collect_beepers_in_all_columns():
    while front_is_clear():
        beeper_count = collect_beepers_in_this_column()
        put_collected_beepers(beeper_count)
        move()
    beeper_count = collect_beepers_in_this_column()
    put_collected_beepers(beeper_count)

def go_back():
    turn_around()
    while front_is_clear():
        move()
    turn_around()

if __name__ == "__main__":
    run_karel_program("sample_quad1")