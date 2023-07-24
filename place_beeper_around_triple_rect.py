from stanfordkarel import *

def main():
  go_to_corner()

def go_to_corner():
  if facing_north():
    while front_is_clear():
      move()
    turn_left()
    while front_is_clear():
      move()
    turn_around()
  elif facing_south():
    turn_around()
    while front_is_clear():
      move()
    turn_left()
    while front_is_clear():  
      move()
    turn_around()
  elif facing_east():
    turn_left()
    while front_is_clear():
      move()
    turn_left()
    while front_is_clear():
      move()
  elif facing_west():
    turn_right()
    while front_is_clear():
      move()
    turn_right()
    while front_is_clear():
      move()  

def turn_around():
  turn_left()
  turn_left()

def turn_right():
  turn_left()
  turn_left()
  turn_left()

  if __name__ == "__main__":
    run_karel_program("triple_karel")
 