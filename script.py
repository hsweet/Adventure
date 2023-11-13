import actions

'''All the room descriptions and game objects are here.

- They are all in a python dictionary of dictionaries
- objects['key']['usable'] = True
- There should be an entry for each room and object in your game.
- Each room is a function in rooms.py

For the script:
- The key is the room name, and the value is the description
- The room name is enclosed in quotes, followed by a :
- \n makes a new line

Follow and modify the examples below.
'''
objects = {
    'phone': {
        'description': 'a regular cell phone',
        'usable': True,
        'action': actions.use_phone
    },
    'key': {
        'description': 'a small key',
        'usable': True,
        'action': actions.unlock_door
    },
    'book': {
        'description': 'an old book',
        'usable': True,
        'action':actions.read_book
    },
    'note': {
        'description':
        'a crumpled piece of paper with the number 102 barely visible',
        'usable': False
    },
    'door': {
        'description': 'a small door',
        'usable': True,
        'action': actions.read_note
    }

    # Add more objects as needed
}


script = {
    'entry': '''\nThe door squeaks shut behind you.. \n\nIt is quite hard to see\n\nA small bat whizzes by your head''',
    'kitchen': '''\nThere is a little light coming from a small filthy window over the sink''',
    'closet': '''\nYou push some clothes out of the way to uncover a small door''',
    'road': '''It is raining heavily and your car has blown a tire..\n\n You see the light from an old house to the east ''',
    'finish': '''You walk past your flattened Tesla and wearily thumb a ride back to the nearest town\n\n''',
    'secret_room':'The only thing here is a mouse trapped in a cage..\n\n'
}

if __name__ == "__main__":
    print("This code is for testing.  Run script.py from the terminal")
    print('_' * 60 + '\n')
    print(f'These are the objects, {objects.keys()}\n')
    print (f'These are the rooms in your script, {script.keys()}\n')
    print ('If you see all your objects and roooms and not getting any errors, all is good! If not, carefully check your syntax.\n')