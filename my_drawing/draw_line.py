"""
File: draw_line.py
Name:劉映麟
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow() # create a new graphics window
SIZE = 10 # define the size of the hole
count = 0 # initialize the count variable
start_point = None # initialize the start_point variable
line = None # initialize the line variable
hole = None # initialize the hole variable

def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(hole_punch) # call the hole_punch function when the mouse is clicked

def hole_punch(mouse):
    global count, start_point, line, hole
    if count == 0: # check if the user has clicked once
        hole = GOval(SIZE, SIZE) # create a new hole object
        hole.filled = True # fill the hole
        hole.fill_color = "white" # set the hole color to white
        window.add(hole, x=mouse.x, y=mouse.y) # add the hole to the window at the mouse position
        start_point = (mouse.x, mouse.y) # set the start_point variable
    elif count == 1: # check if the user has clicked twice
        end_point = (mouse.x, mouse.y) # set the end_point variable
        line = GLine(start_point[0], start_point[1], end_point[0], end_point[1]) # create a new line object
        window.add(line) # add the line to the window
        window.remove(hole) # remove the hole from the window
        start_point = None # reset the start_point variable
    else: # if the user has clicked more than twice
        count = 0 # reset the count variable
        hole = GOval(SIZE, SIZE) # create a new hole object
        hole.filled = True # fill the hole
        hole.fill_color = "white" # set the hole color to white
        window.add(hole, x=mouse.x, y=mouse.y) # add the hole to the window at the mouse position
        start_point = (mouse.x, mouse.y) # set the start_point variable
    count += 1 # increment the count variable by 1

if __name__ == '__main__':
    main()
