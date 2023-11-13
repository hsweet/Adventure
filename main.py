import intro
import rooms
import play
from time import sleep
import os


os.system('clear')
'''
This file just starts the game.

- The play module contains functions to run the game, such as move around, get descriptions, pick up and use things.

- All the room functions are in rooms.py.

- actions.py has all the functions that are called to use objects in your inventory Everything in the game that does something has a function.

- script.py has the script and object list as python dictionarys.

- vocab.py contains vocabulary for the game. It is not being used yet

'''
def intro():
  play.typewrite('''\nYour car has broken down on a dark, rainy night.
\nYou can see a light from an old mansion behind an iron gate thru the woods\n'''
        )
  answer = input('\nWalk to house? y/n..')
  answer = answer[0].lower()  # clean up input
  if answer == 'y':
    rooms.entry()
  else:
    play.typewrite(
       '''\nYou chose to stay in your car.  The wind gets stronger and stronger.  There is no cell signal. You wait.
\n\nA large tree falls on your car''')
    sleep(1)
    os.system('clear')
    print('''
### #           ###       #
 #  ### ###     #   ##  ###
 #  # # ##      ##  # # # #
 #  # # ###     #
 #  # # ###
 #              ###
''')
if __name__ == "__main__":
  #intro.wrapper(intro.center, "Birch Rescue Squad")  # Use your title

  if input('Load saved game? (y/n) ').lower() == 'y':
    play.load_game_state()    # load last game
  else:
    intro()    # start a new game
