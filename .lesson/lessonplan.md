# Lesson plan

Things to add..
1. typewrite()
2. grammer.  decide when to use a, an or plural
3. hunger.  (You can get pizza delivered with the phone)
4. phone numbers to call.. use phone ==> dial function check for correct number
5. battery bar display

## Description

This code is creating a text-based game where the player navigates through different rooms in a mansion. The main.py file contains the main logic of the game.

The code starts by importing necessary modules such as os, json, actions, and a script from a script module. It then clears the console using os.system('clear').

There is an inventory list initialized with a single item "phone". The code defines objects in the game, such as a phone, key, book, note, and safe. Each object has a description and usability. Some objects also have associated actions defined in the actions module.

There is a dictionary room_functions that maps room names to corresponding functions. This is used to navigate between rooms based on player choices.

The code defines several functions for different rooms like entry(), kitchen(), closet(), and finish(). Each function represents a different room in the mansion and has defined exits and objects in the room. The print_room_description() function is used to print the description of the current room and the objects in it.

The navigate() function is used to handle user input and allow the player to navigate between rooms or perform actions based on available exits and objects. It also handles commands like taking objects, using objects, displaying inventory, showing game instructions, and quitting the game.

The code also includes some utility functions like take_object(), use_object(), and print_room_description() to perform specific actions within the game.

At the end of the code, it checks if the game should be loaded from a saved state or started fresh. If loading a saved game is chosen, the previous game state is loaded from a JSON file. Otherwise, the intro() function is called to start the game.

The actions.py file contains various action functions that can be performed in the game. These functions include using the phone, unlocking a door, reading a note, and displaying game help.

Overall, the code allows the player to explore different rooms, interact with objects, and progress through the game by making choices. The actions and functionalities of the game are defined in separate functions and modules to keep the code organized and modular.