import actions
import json
import os
import rooms

file_path = os.getcwd()
# Saving game state to a JSON file in the current directory
def save_game_state(game_state):
  #file_path = os.getcwd()
  try:
    with open(file_path + '/game_state.json', 'w') as file:
      json.dump(game_state, file)
  except FileNotFoundError:
    print('Can\'t find the file to save to ')

# Loading game state from a JSON file in the current directory
# room_functions is requiring a circular import.
def load_game_state():
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
      game_state = json.loads(file_contents)
      inventory = game_state[0]
      actions.update_inventory(inventory)
      current_room = game_state[1]
      actions.charge = game_state[2]
      room_functions[current_room]()
  except FileNotFoundError:
    print("No saved game state found. Starting new game...\n")
    room_functions['entry']()


def load_game_state0():
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
      print (game_state[0])
      actions.inventory = game_state[0]   # this ends the game somehow.
      current_room = game_state[1]
      actions.charge = game_state[2]
      room_functions[current_room]()
  except FileNotFoundError:
    print("No saved game state found. Starting new game...\n")
    room_functions[current_room]()

if __name__ == '__main__':
  load_game_state()