import os
from random import randint
from time import sleep

# global variables
charge = 10  # phone is fully charged
cell_signal = 10

os.system('clear')

def use_phone():
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

def unlock_door():
    print('Door unlocked!')

def read_note():
  # add the ability to use phones light to read
  print('''You try to read the waterstained note.\nIt is too dark to read\n You decide to head back to the kitchen.''')

def game_help():
  os.system('clear')
  print('''
  Your car has broken down and now you find youself in a deserted house.  You can ....
  ''')

if __name__ == "__main__":  #only runs if this is not being used as a module!
    game_help()
    #use_phone()