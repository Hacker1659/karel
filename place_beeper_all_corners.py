

def main():
  place_beepers_everywhere()

def turn_around():
  turn_left()
  turn_left()

def place_beepers_row():
  turn_left()
  while front_is_clear():
    if not beepers_present():
      put_beeper()
    move()
  if not beepers_present():
    put_beeper() 

def place_beepers_everywhere():
  while front_is_clear():  
      place_beepers_row()
      go_back()
      move()
  place_beepers_row()

def go_back():
  turn_around()
  while front_is_clear():
    move()
  turn_left()

if __name__ == "__main__":
    run_karel_program("sample_quad1")
   
   