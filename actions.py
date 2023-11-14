import os
from random import randint
from time import sleep

####################################################################################################
#                                        Leave as is!                                              #
####################################################################################################
# global variables
charge = 10  # phone starts fully charged
cell_signal = 10
inventory = ['phone']
visited_rooms = {}

# these 2 functions restore
#  a saved game
def update_inventory(new_inventory):
    global inventory
    for item in new_inventory:
        if item not in inventory:
            inventory.append(item)

def update_visited_rooms(new_rooms):
    global visited_rooms
    visited_rooms.update(new_rooms)

os.system('clear')


####################################################################################################
#      Put all action functions below. def your_room(room_name) the parameter is required          #
####################################################################################################

def use_phone(room_name, answer = 4):  # remove answer after testing!
  # add code to drain battery each time used
  # the way out could be the correct extension
  os.system('clear')
  global charge
  extension = 102
  print(' Battery'.center (30))
  # make a battery bar display
  print('---------|'.center (30))
  for i in range(charge):
    #print(f'{i*"█"}{(charge-i)*"░"}'.center(20, ' '))
    print ("\r" + "#" * i, end = "".center(30))
    sleep(0.2)
  print ('\n')
  charge -= 1  # losing power
  if charge == 0:
    print('\n Game over ..')
    exit()
  #answer = randint(1, 4)
  if answer == 1:  # no answer
    ring(10)
    print('\n\n> Click.')
  elif answer == 2:
    ring(4)
    print(
        "BEEP..\n\n> The number you wish to call cannot be completed as dialed ")
  elif answer == 3:
    ring(3)
    sleep(1)
    print(
        "\nThe party you wish to reach is not available, please leave a message after the beep"
    )
    sleep(1)
    print('\nBEEP!\n')
    input('\nyour meassage? ')    # should I save the message?
  else:
    ring(4)
    print(
        '''\n\n>  Welcome to Birch Rescue Services. \n\n> If you know your partie\'s extension, you may dial it at any time
\n\n> Please pay careful attention to this message as our options have changed.
\n\n> For help, dial 1, to register a complaint, dial 2, for food delivery, dial 3.
\n\n> Dial 4 to speak with an operator, or stay on the line and a representative will be with you shortly.
\n\n> (tuneless phone music plays endlessly )''')
  response = str(input('\n> Please choose an option .. '))
  if response == "1" or response == "2":
    print ("Sorry we missed you, please call during normal business hours")
    for i in range (20):
      print ("\r" + "#" * i, end = "")
      sleep (.5)
  elif response == "3":
    pizza()
  elif response == "4":
    print ('''> Welcome.. Your location has been established.. Help is on the way''')

def pizza():
  print('pizza is delivered...')

def ring(times):
  for _ring in range(times):
    print("Ring", end=", ")
    sleep(1)

def read_book(room_name):
  print ('Look\'s like it is written in Chinese.  You don\'t understand it.')


def unlock_door(room_name):
  if room_name == 'closet':
    os.system('clear')
    print(f'You hear a click.')
    print(f'\nThe safe is unlocked in {room_name}!')
    print(
        '''You hear a click. The door swings open. You can see a table with a bunch of papers on it.''')


def read_note(room_name):
  # add the ability to use phones light to read
  print(
      '''You have to use your phone's flashlight to read the waterstained note.\n\n> It seems to be an advert for a pizza joint.\n\n>
It reads: "Call us at 555-0110 for fast pizza delivery.  There is a second number scribbled in pencil..   It looks like B.R.S. 555-0220.\n\n> '''
  )

def secret_room(room_name):
  print ('secret room function')

def game_help(room_name):
  os.system('clear')
  print('''
  Your car has broken down and now you find youself in a deserted house.  You can ....
  ''')


if __name__ == "__main__":
  use_phone('bed')
  # print(inventory)