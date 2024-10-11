from tkinter import *
import settings # import du fichier settings
import utils

root  = Tk() # Window instanciation. Tk stands for toolkit and was developed as the GUI library for the scripting language tcl (tool command language).
# Overide the setting of window
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}") # root.geometry("width x height"). Defines the size of the window
root.title("Minesweep boy !") # set the title of the page
root.resizable(False, False) # window can't change size

# Defining frames in the window
top_frame = Frame(
    root, # where it should display
    bg = "red", # background color # TODO change later
    width=utils.width_prct(25),
    height =utils.height_prct(25)
    ) 

# WHERE the frame should be starting, px value, sur les axes x & y
top_frame.place(
    x = 0, 
    y = 0
)

left_frame = Frame(
    root, # where it should display
    bg = "blue", # background color # TODO change later
    width= 360,
    height = 540
    ) 

left_frame.place(
    x = 0, 
    y = 180
)


# Run the window
root.mainloop() # displays the window and waits for the user's action
