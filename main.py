import actions
import intro
import json
import os
import play
import rooms
from time import sleep

file_path = os.getcwd()
os.system('clear')
'''
Start a new game or load previous.

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

def load_game_state():
  # loads last game

  room_functions = {
      'entry': rooms.entry,
      'kitchen': rooms.kitchen,
      'closet': rooms.closet,
      'secret_room':rooms.secret_room
      # Add more room names and functions as needed
  }
  try:
    with open(file_path + '/game_state.json', 'r') as file:
      file_contents = file.read()
      if not file_contents:  # Check if the file is empty
        print("No saved game state found. Starting new game...\n")
        room_functions['entry']()
        return

      # load and parse saved game
      game_state = json.loads(file_contents)
      inventory = game_state[0]
      actions.update_inventory(inventory)
      current_room = game_state[1]
      actions.charge = game_state[2]
      previous_visits = game_state[3]
      actions.update_visited_rooms(previous_visits)

      # go to saved room
      room_functions[current_room]()

  except FileNotFoundError:
    print("No saved game state found. Starting new game...\n")
    room_functions['entry']()


if __name__ == "__main__":
  #intro.wrapper(intro.center, "Birch Rescue Squad")  # Use your title

  if input('Load saved game? (y/n) ').lower() == 'y':
    load_game_state()    # load last game
  else:
    intro()    # start a new game
