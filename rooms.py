 
from play import *

 
#########################  Rooms ########################

def intro():
  typewrite('''\nYour car has broken down on a dark, rainy night.
\nYou can see a light from an old mansion behind an iron gate thru the woods'''
        )
  ans = input('\nWalk to house? y/n..')
  ans = ans[0].lower()  # clean up input
  if ans == 'y':
    entry()
  else:
    typewrite(
        '''\nYou chose to stay in your car.  The wind gets stronger and stronger.  There is no cell signal. You wait.
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

def introduction():
  # if you want it. 
  pass


def road():
  this_room = 'road'
  exits = {'e': entry}
  objects_in_room = []  # No objects in this room
  print_room_description(this_room, objects_in_room)
  key, destination = navigate(exits, this_room, objects_in_room)
  destination()


def kitchen():
  this_room = 'kitchen'
  exits = {'e': finish, 's': entry}
  objects_in_room = ['book']  # Objects available in this room
  objects_in_room = [obj for obj in objects_in_room if obj not in inventory]
  print_room_description(this_room, objects_in_room)
  key, destination = navigate(exits, this_room, objects_in_room)
  destination()


def entry():
  this_room = "entry"
  exits = {'n': kitchen, 's': closet}
  objects_in_room = ['key']  # Objects available in this room
  objects_in_room = [obj for obj in objects_in_room if obj not in inventory]
  print_room_description(this_room, objects_in_room)
  key, destination = navigate(exits, this_room, objects_in_room)
  destination()


def closet():
  this_room = 'closet'
  exits = {'n': entry}
  objects_in_room = ['door']
  objects_in_room = [obj for obj in objects_in_room if obj not in inventory]
  print_room_description(this_room, objects_in_room)
  key, destination = navigate(exits, this_room, objects_in_room)
  destination()

def secret_room():
  '''This is accessed when the user unlocks the door  '''''
  this_room = 'secret_room'
  exits = {'n': kitchen} 
  objects_in_room = []
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