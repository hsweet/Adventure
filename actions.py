import os
from random import randint
from time import sleep


'''Put all action functions here. def room(room_name) the parameter is required even if the function does not use it'''

# global variables
charge = 10  # phone is fully charged
cell_signal = 10

os.system('clear')

def use_phone(room_name):
    # add code to drain battery each time used
    # the way out could be the correct extension
    os.system('clear')
    global charge
    extension = 102
    print (f'Phone charge is {charge}\n')
    charge -=1   # losing power
    if charge == 0:
        print('\n Game over ..')
        exit()
    answer = randint(1,4)
    if answer == 1:   # no answer
        ring(10)
        print ('\n\nClick.')
    elif answer == 2:
        ring(4)
        print("BEEP..\n\nThe number you wish to call cannot be completed as dialed ")
    elif answer == 3:
        ring(3)
        sleep(1)
        print ("\nThe party you wish to reach is not available, please leave a message after the beep")
        sleep (1)
        print ('\nBEEP!\n')
        input ('\nyour meassage? ')
    else:
        ring (4)
        print ('''\n\nWelcome to Birch Rescue Services. \\nIf you know your parties extension, you may dial it at any time
\n\nPlease pay careful attention to this message as our options have changed.
\nFor help, dial 1, to register a complaint, dial 2, for food delivery, dial 3.
\nDial 4 to speak with an operator, or stay on the line and a representative will be with you shortly.
\n\n(tuneless phone music plays endlessly )''')
        input( 'Dial extension? .. ')
        if extension == 102:
            print ("you have reached the office of .   ")

def ring(times):
    for _ring in range (times):
        print ("Ring", end = ", ")
        sleep (1)

def unlock_door(room_name):
    if room_name == 'closet':
        os.system('clear')
        print(f'You hear a click.')
        print(f'\nThe safe is unlocked in {room_name}!')
        print('''\nYou open the door and pick up the small electronic device inside\n\n
Holy Cow! It is a power bank that fits your phone!''')
    else:
        print('\nThere is nothig to unlock here.')

def read_note(room_name):
  # add the ability to use phones light to read
  print('''You try to read the waterstained note.\nIt is too dark to read\n You decide to head back to the kitchen.''')

def game_help(room_name):
  os.system('clear')
  print('''
  Your car has broken down and now you find youself in a deserted house.  You can ....
  ''')

#if __name__ == "__main__":