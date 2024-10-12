from tkinter import *
from cell import Cell # import the Cell class from the file cell.py
import settings # import du fichier settings
import utils
import random 


root  = Tk() # Window instanciation. Tk stands for toolkit and was developed as the GUI library for the scripting language tcl (tool command language).
# Overide the setting of window
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}") # root.geometry("width x height"). Defines the size of the window
root.title("Minesweep boy !") # set the title of the page
root.resizable(False, False) # window can't change size

# Defining frames in the window
top_frame = Frame(
    root, # where it should display
    bg = "#640D5F", # background color # TODO change later
    width=settings.WIDTH,
    height =utils.height_prct(25)
    ) 

# WHERE the frame should be starting, px value, sur les axes x & y
top_frame.place(
    x = 0, 
    y = 0
)

left_frame = Frame(
    root, # where it should display
    bg = "#640D5F", # background color # TODO change later
    width= utils.width_prct(25),
    height =utils.height_prct(75)
    ) 

left_frame.place(
    x = 0, 
    y =utils.height_prct(25)
)

center_frame = Frame(
    root, # where it should display
    bg = "#640D5F", # background color # TODO change later
    width= utils.width_prct(75),
    height =utils.height_prct(75)
)

center_frame.place(
    x = utils.width_prct(25), 
    y =utils.height_prct(25)
)

# USING THE GRID METHOD TAKES THE PARENT ELEMENT HERE, CENTER FRAME, AND DIVIDES IT INTO COLUMNS AND ROWS   
for x in range (settings.GRID_SIZE):
    for y in range (settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column = x,
            row= y
        )

Cell.randomize_mines()


root.mainloop() # displays the window and waits for the user's action