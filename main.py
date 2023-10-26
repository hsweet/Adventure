import os
from time import sleep
import actions

os.system('clear')

# Define objects
objects = {
    'phone':{'description':'a regular cell phone','usable':True,'action':actions.use_phone},
    'key': {'description': 'a small key', 'usable': True, 'action': actions.unlock_door},
    'book': {'description': 'an old book', 'usable': False},
    'note':{'description':'acrumpled piece of paper with the number 102 barely visible', 'usable':False}
    # Add more objects as needed  or add a note function to make user solve a puzzle to get the message
}
# define descriptions
dialog = {
    'entry': '''\nThe door squeaks shut behind you.. \nIt is quite hard to see\n A small bat whizzes by your head''',
    'kitchen': '''\nA musty kitchen.  There is a little light coming from a small filthy window over the sink''',
    'closet': '''\nThere is nothing here''',
    'road':'''It is raining heavily and your car has blown a tire.. You see the light from an old house to the east ''',
    'finish':'''You walk past your flattened Tesla and wearily thumb a ride back to the nearest town\n\n'''
}

# Player's inventory
inventory = ['phone']

def intro():
    print('''\nYour car has broken down on a dark, rainy night.
\nYou can see a light from an old mansion behind an iron gate thru the woods''')
    ans = input ('\nWalk to house? y/n..')
    ans = ans[0].lower()    # clean up input
    if ans == 'y':
        entry()
    else:
        print ('''\nYou chose to stay in your car.  The wind gets stronger and stronger.  There is no cell signal. You wait.
\n\nA large tree falls on your car''')
        sleep(1)
        os.system('clear')
        print('''
### #           ###       #
 #  ### ###     #   ##  ###
 #  # # ##      ##  # # # #
 #  # # ###     #   # # ###
 #              ###
''')

def road():
    this_room = 'road'
    exits = {'e': entry}
    objects_in_room = []  # No objects in this room
    print_room_description(this_room, objects_in_room)
    key, destination = navigate(exits, this_room, objects_in_room)
    destination()

def kitchen():
    this_room = 'kitchen'
    exits = {
        'e': finish,
        's': entry
    }
    objects_in_room = ['book']  # Objects available in this room
    objects_in_room = [obj for obj in objects_in_room if obj not in inventory]
    print_room_description(this_room, objects_in_room)
    key, destination = navigate(exits, this_room, objects_in_room)
    destination()

def entry():
    this_room = "entry"
    exits = {
        'n': kitchen,
        's': closet
    }
    objects_in_room = ['key']  # Objects available in this room
    objects_in_room = [obj for obj in objects_in_room if obj not in inventory]
    print_room_description(this_room, objects_in_room)
    key, destination = navigate(exits, this_room, objects_in_room)
    destination()

def closet():
    this_room = 'closet'
    exits = {'n': entry}
    objects_in_room = []  # No objects in this room
    objects_in_room = [obj for obj in objects_in_room if obj not in inventory]
    print_room_description(this_room, objects_in_room)
    key, destination = navigate(exits, this_room, objects_in_room)
    destination()

def finish():
    print(dialog['finish'])
    sleep(2)
    print('''
### #           ###       #
 #  ### ###     #   ##  ###
 #  # # ##      ##  # # # #
 #  # # ###     #   # # ###
 #              ###
''')
    #print ('The End!')
###################################################### General Functions #################

def print_room_description(room, objects_in_room):
    os.system('clear')
    l = len (room) + 15
    print ('*'* l)
    print(f'* You are in {room} *')
    print ('*'* l + '\n')
    #print('Objects in the room:')
    i = ", ".join(inventory)
    print(f'You have {i}\n')
    for obj in objects_in_room:
        print(f'- There is a {objects[obj]["description"]}')
    print(dialog[room])

def navigate(exits, current_room, objects_in_room):
  while True:
      if len(objects_in_room) > 0:
          print('\nYou see the following objects:')
          for obj in objects_in_room:
              print(f'- {obj}')

      print('\nCommands: n(orth), e(ast), s(outh), w(est), t(ake), u(se), i(nventory), h(elp) q(uit) ')
      choice = input('\nWhat would you want to do? .. ')

      if choice in exits:   # a valid exit
          os.system('clear')
          return choice, exits[choice]
      elif choice == 't':
          take_object(objects_in_room)
          continue
      elif choice == 'u':
          use_object(inventory)
          continue
      elif choice == 'i':
          i = ", ".join(inventory)
          print(f'\nYou have {i}\n')
          continue
      elif choice == 'h':
          actions.game_help()
          continue
      elif choice == 'q':
          os.system('clear')
          quit()

      os.system('clear')
      print("\nInvalid command. Try again.\n")
  
def take_object(objects_in_room):
# needs code to remove object from room when taken
    obj_to_take = input('What would you want to take: ')
    if obj_to_take in objects_in_room:
        objects_in_room.remove(obj_to_take)
        inventory.append(obj_to_take)
        print(f'\nYou took the {obj_to_take}')
    else:
        print('\nThat object is not in the room.')



def use_object(inventory):
    if not inventory:
        print('\nYou have no objects in your inventory.')
        return

    print('\nYou have the following objects in your inventory:')
    for obj in inventory:
        print(f'- {obj}')

    obj_to_use = input('Enter the name of the object you want to use: ')
    if obj_to_use in inventory:
        if 'action' in objects[obj_to_use]:
            action = objects[obj_to_use]['action']
            print(f'\nYou used the {obj_to_use}.')
            action()  # Call the function reference
        else:
            print(f'\nYou cannot use the {obj_to_use}.')
    else:
        print('\nYou do not have that object in your inventory.')


if __name__ == "__main__":
    intro()