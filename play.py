import actions
import os
import json
from script import *
import sys
from time import sleep


inventory = actions.inventory
visited_rooms = actions.visited_rooms
file_path = os.getcwd()


########### General Functions #################

def previously_visited(room):
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


def print_room_description(room, objects_in_room, increment = True):
  """
    Prints the description and objects in the current room and saves the state of the game.
    """
  os.system('clear')
  print(f'> You are in {room}\n ')
  if increment == True:
    visits = previously_visited(room)  # increment visit count
    # decorate room name
    l = len(room) + 15
    #print('*' * l)
    print(f'> You have been here {visits} times.\n')
    #print('*' * l + '\n')
  else:
    os.system('clear')
    typewrite(script[room])

  # prints long description only on first visit
  if visited_rooms[room] < 2:
    i = ", ".join(inventory)
    print(f'> You have {i}\n')
    for obj in objects_in_room:
      print(f'> There is a {objects[obj]["description"]}')
    typewrite(script[room])
  print('\n'+'_' * 30)
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


def navigate(exits, current_room, objects_in_room):
  """
    Navigate to other rooms or perform actions based on the available exits and objects.

    """
  while True:
    if len(objects_in_room) > 0:
      print('\n> You see the following objects:\n')
      for obj in objects_in_room:
        print(f'- {obj}')

    print(
        '\n> Commands: \n\n> n(orth), e(ast), s(outh), w(est), t(ake), u(se), i(nventory), h(elp), l(ook), q(uit) '
    )
    choice = input('\n> What do you want to do? .. ')
    if choice:
      choice = choice[0].lower()  #  cleans input ==> first letter, lower case
    # print (f'Choice is {choice}')

    if choice in exits:  # is this a valid exit?
      os.system('clear')
      return choice, exits[choice]

    # other commands
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
    elif choice == 'l':
      print ("Looking")
      print_room_description(current_room, objects_in_room, increment=False)
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
  obj_to_take = input('\n> What do you want to take: ')
  if obj_to_take in objects_in_room:
    objects_in_room.remove(obj_to_take)
    inventory.append(obj_to_take)
    print(f'\nYou took the {obj_to_take}')
    os.system('clear')
  else:
    typewrite('\n> That object is not in the room.')


def use_object(inventory, this_room):
  """
    Prompts the user to use an object from their inventory.
    Performs the corresponding action based on the selected object.
    """
  if not inventory:
    print('\n> You have no objects in your inventory.')
    return

  print('\n> You have the following objects in your inventory:')
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
      print(f'\n> You cannot use the {obj_to_use}.')
  else:
    print('\n> You do not have that object in your inventory.')
