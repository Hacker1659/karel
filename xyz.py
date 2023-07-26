from stanfordkarel import *
 
def main():
  move_forward_east()
  move_forward_west()

def turn_right():
  turn_left()
  turn_left()
  turn_left()

def come_down():
  while front_is_clear():
    move()

def move_forward_east():
  while True:
    if facing_west():
      turn_left()
      come_down()
      turn_right()
      break
    if front_is_clear() and right_is_blocked():
        move()
    if right_is_clear():
      turn_right()
      move()
    if front_is_blocked():
      turn_left()

def move_forward_west():
  while True:
    if facing_east():
      turn_right()
      come_down()
      turn_left()
      break
    if front_is_clear() and left_is_blocked():
      move()
    if left_is_clear():
      turn_left()
      move()
    if front_is_blocked():
      turn_right()  
if __name__ == "__main__":
  run_karel_program("/Users/anirudh/Workspace/GitHub/karel/worlds/wall_world1.w")