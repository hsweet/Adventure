import actions
import json
import os
from script import script
#from rooms import *
import rooms
import sys
from time import sleep
# import vocab

os.system('clear')
file_path = os.getcwd()

################### General Functions #################

# Saving game state to a JSON file in the current directory
def save_game_state(game_state):
  #file_path = os.getcwd()
  try:
    with open(file_path + '/game_state.json', 'w') as file:
      json.dump(game_state, file)
  except FileNotFoundError:
    print('Can\'t find the file to save to ')

# Loading game state from a JSON file in the current directory

def load_game_state():
  # used to load saved rooms, used by itself.
  room_functions = {
      'entry': rooms.entry,
      'kitchen': rooms.kitchen,
      'closet': rooms.closet
      # Add more room names and functions as needed
  }
  try:
    with open(file_path + '/game_state.json', 'r') as file:
      game_state = json.load(file)
      game_state[0]
      current_room = game_state[1]
      actions.charge = game_state[2]
      room_functions[current_room]()
  except FileNotFoundError:
    print("No saved game state found. Starting new game...\n")
    room_functions[current_room]()

    os.system('clear')
    print("\nInvalid command. Try again.\n")



if __name__ == "__main__":

  # used to load saved rooms
  if input('Load saved game? (y/n) ').lower() == 'y':
    load_game_state()
  else:
    rooms.intro()
