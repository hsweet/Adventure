import actions
import os
import json
# import rooms
from script import *
import sys
from time import sleep


inventory = actions.inventory
#inventory =['phone']
visited_rooms = {}
file_path = os.getcwd()


########### General Functions #################

def visited(room):
  '''
  How many times has room been visited?
  '''
  if room in visited_rooms:
    visited_rooms[room] += 1
  else:
    visited_rooms[room] = 1
  return visited_rooms[room]


def typewrite(message):
  '''from https://www.youtube.com/watch?v=2h8e0tXHfk0'''
  for char in message:
    sys.stdout.write(char)
    sys.stdout.flush()
    if char != '\n':
      sleep(0.05)
    else:
      sleep(1)


# add a flag parameter to replay description from a look command
def print_room_description(room, objects_in_room):
  """
    Prints the description and objects in the current room and saves the state of the game.
    """
  os.system('clear')
  vst = visited(room)
  # decorate room name
  l = len(room) + 15
  print('*' * l)
  print(f'* You are in {room} *')
  print(f'You have been here {vst} times.')
  print('*' * l + '\n')
  # prints long description only on first visit
  # be good to add a look command if you want that again
  if visited_rooms[room] < 2:
    i = ", ".join(inventory)
    print(f'You have {i}\n')
    for obj in objects_in_room:
      print(f'- There is a {objects[obj]["description"]}')
    typewrite(script[room])
  print('\n'+'*' * 60)
  game_state = [inventory, room, actions.charge, visited_rooms]
  save_game_state(game_state)


# Saving game state to a JSON file in the current directory
def save_game_state(game_state):
  #file_path = os.getcwd()
  try:
    with open(file_path + '/game_state.json', 'w') as file:
      json.dump(game_state, file)
  except FileNotFoundError:
    print('Can\'t find the file to save to ')
'''
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
      game_state[0]
      current_room = game_state[1]
      actions.charge = game_state[2]
      room_functions[current_room]()
  except FileNotFoundError:
    print("No saved game state found. Starting new game...\n")
    room_functions['entry']()


def load_game_state0():
  # used to load saved rooms, used by itself.
  room_functions = {
      'entry': entry,
      'kitchen': kitchen,
      'closet': closet
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
'''

def navigate(exits, current_room, objects_in_room):
  """
    Navigate to other rooms or perform actions based on the available exits and objects.

    """
  while True:
    if len(objects_in_room) > 0:
      print('\nYou see the following objects:')
      for obj in objects_in_room:
        print(f'- {obj}')

    print(
        '\nCommands:   ************* \n\nn(orth), e(ast), s(outh), w(est), \n\nt(ake), u(se), i(nventory), h(elp), \n\nl(ook), q(uit) '
    )
    choice = input('\nWhat do you want to do? .. ')
    if choice:
      choice = choice[0].lower()  #  cleans input ==> first letter, lower case

    if choice in exits:  # is this a valid exit?
      os.system('clear')
      return choice, exits[choice]
    elif choice == 't':
      take_object(objects_in_room, current_room)
      continue
    elif choice == 'u':
      use_object(inventory, current_room)  # Pass the current_room parameter
      continue
    elif choice == 'i':
      i = ", ".join(inventory)
      print(f'\nYou have {i}\n')
      continue
    elif choice == 'h':
      actions.game_help(current_room)
      continue
    elif choice == 'q':
      os.system('clear')
      quit()

    os.system('clear')
    print("\nInvalid command. Try again.\n")


def take_object(objects_in_room, current_room):
  """
    Prompts the user to take an object from the room.
    Adds the object to the inventory if it exists in the room.
    """
  obj_to_take = input('\nWhat do you want to take: ')
  if obj_to_take in objects_in_room:
    objects_in_room.remove(obj_to_take)
    inventory.append(obj_to_take)
    print(f'\nYou took the {obj_to_take}')
    os.system('clear')
  else:
    typewrite('\nThat object is not in the room.')


def use_object(inventory, this_room):
  """
    Prompts the user to use an object from their inventory.
    Performs the corresponding action based on the selected object.
    """
  if not inventory:
    print('\nYou have no objects in your inventory.')
    return

  print('\nYou have the following objects in your inventory:')
  for obj in inventory:
    print(f'- {obj}')

  obj_to_use = input('Enter the name of the object you want to use: ')
  if obj_to_use in inventory:
    if 'action' in objects[obj_to_use]:
      action = objects[obj_to_use]['action']  # Pass the function reference
      print(f'\nYou used the {obj_to_use}.')
      os.system('clear')
      action(this_room)  # Pass the room name argument to the function
      # one possible way to impliment special action for a particular room
      if this_room == "closet":
        actions.secret_room(this_room)
    else:
      print(f'\nYou cannot use the {obj_to_use}.')
  else:
    print('\nYou do not have that object in your inventory.')