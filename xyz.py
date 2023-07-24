from stanfordkarel import *
 
def main():
  while front_is_clear(): 
    move()

def turn_around():
 turn_left()
 turn_left()
  
if __name__ == "__main__":
  run_karel_program("/Users/anirudh/Workspace/GitHub/karel/worlds/karel1.w")