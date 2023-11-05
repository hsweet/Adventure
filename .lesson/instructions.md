## Instructions

You will work together with a partner to build a text adventure game. 

[Wikipedia article](https://en.wikipedia.org/wiki/Text-based_game)

[A student game](https://replit.com/@awam/MountainTop-or-AI-Adventure-Game?v=1)

Text games were very popular back in the day.  The day being fancy computer graphics, good sound, and now VR.

But they still have a lot of the basic elements of a good game.  You tmake the graphics in your mind.  Kind of like the difference between a book and a movie based on a book.

I think this a great project for a beginning programmer.  There are more than enough things to learn working on a game like this, all of which you would need to know to go further. 

I have written the harder bits, all as functions.  It is no different than using turtle functions.  I do not know or care about how turtle.right() works and you do not need to know how navigate() works in this game to navigate.

My hope is that you study navigate() and some of my functions, and try to understand what is happening, but it will do it's thing regardless :)

## How to start

To start, you need a written game description, a map, a list of all the items in your rooms, what happens when a player uses an item.  Follow the patterns in my code.

![Game Map](assets/map.jpg)

You map should show the name of the room, the ways out (exits) and any items found in the room.  You will write each of your rooms as a function.  You can modify the rooms in the sample game to start.

You can also add your own functions to the game.  For example you might write a goto_random_room() function.

## Files

I decided to break up this large program into several files.  This makes it easier to debug and less confusing.  

|File|Function|
|---|---|
|main.py|object list, room function and general functions| 
|intro.py|experimental splash screen using Python curses|
|actions.py|functions for using objects|
|script.py|all the room descriptions|
|game_state.json|games are saved to this file as you play|
|vocab.py|code to improve game's vocabulary|

## Coding..

Most of the data in this game is stored as [Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp).  Visit the link before going further.

###  Objects
Make sure you have a good map!  In this example, phone is the key.  You need a description and `usable` must be set to True or False.  If `usable == True` you need to have an action.  An action is just a function in the actions.py file.  Using the phone triggers actions.use_phone()

Be careful *not to quote the action*  Python will think it is a string and not a function!  (silly Python).  

```python
objects = {
'phone': {
    'description': 'a regular cell phone',
    'usable': True,
    'action': actions.use_phone
},
  ```
### Object Functions
If an obect has an action the program will try to run the function with the name you wrote in the actions.py file.  The function definition will look like this `def use_phone(room_name):` 

`room_name` is required, even if you don't need it.

### Room Functions Dictionary
Find this in main.py.  Change the names to match the rooms in your game
```python
room_functions = {
  # this needs to be loaded after room functions
    'entry': entry,
    'kitchen': kitchen,
    'closet': closet
    # Add more room names and functions as needed
}
```
### Script
Instructions are in the [script.py](script.py) file.  Again, make sure to use the correct room names.  Triple quotes allow for very long lines to be used in a single `print()` 

### Note about game save

My game saves the player's location, inventory and battery charge.  You might need to change that. 


This is the line in main.py to change`game_state = [inventory, room, actions.charge]`  As an example, your game might have levels, maybe stored as a global variable. Change the list to  `game_state = [inventory, room, level]` (or maybe actions.level, if that is the file level lives in).  You can make the list longer or shorter, depending on what you need to save.

## List of game functions and objects in main.py
You have to write all the functions in actions.py.  Those control what happens whenever you use an object. 

You need to modify all the things in the table that have a *.
Warning!  Don't mess with the other functions thoughtlessy 

|Type|Name|Purpose|
|---|---|---|
|list|inventory|a global list of things you have|
|dictionary|* objects|all the objects in the game |
|function* intro|a curses spash screen |
|function|* introduction|game starts here|
|function|* road|room function|
|function|* kitchen|room function|
|function|* entry|room function |
|function|* closet|room function |
|function|* finish|room function |
|dictionary|* room_funtions|room name:action|
|function|typewrite|fancy text|
|function|visited|how many vists to each room|
|function|print_room_description| |
|function|save_game_state| |
|function|load_game_state| |
|function|navigate| |
|function|take_object| |
|function|use_object| |

