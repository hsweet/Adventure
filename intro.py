import curses
from curses import wrapper
from curses.textpad import Textbox, rectangle

#https://docs.python.org/3/howto/curses.html

def center(screen, message):
  '''Display a message in the center of the screen'''
  
  screen.clear()
  cols, rows = curses.COLS, curses.LINES  # find size of window
  curses.curs_set(0)   # turn off cursor
  curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_GREEN)
  screen.bkgd(' ', curses.color_pair(1) | curses.A_BOLD)
  
  # find centers of screen message
  y, x = rows / 2, cols / 2
  y = int(y)
  x = int(x)
  l = len(message)
  center = int(l / 2)  # center of message

  screen.addstr(y-10 , x-center-5, "Welcome to Text Adventure Game", curses.A_REVERSE)
  screen.addstr(y, x - center, message, curses.A_REVERSE)
  rectangle(screen, y - 4, x - center - 2, y + 4, x + center + 2)
  rectangle(screen, y - 5, x - center - 4, y + 5, x + center + 4)
  screen.addstr(rows-1, 5, 'press any key to quit', curses.A_COLOR)

  screen.refresh()
  screen.getkey()  # wait for a keypress

if __name__ == '__main__':
  
  wrapper(center, "Birch Rescue Squad")
