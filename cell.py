from tkinter import Button
import random # library that gives random object

class Cell :
    all = []
    def __init__(self, x, y, is_mine = False): # passing x and y to define position
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x,
        self.y = y
    
    
    # Append the object to the Cell.all list (= array)
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button( # instance du bouton qui servira de cellule
            location, 
            width =12, 
            height=4,
            text=f"{self.x}, {self.y}"
        )
        # BIND IS USED TO ASSOCIATE A EVENT TO A FUNCTION
        btn.bind("<Button-1>", self.left_click_actions) # convention in tkinter for the left click, we are only passing the reference of the function so no ()
        btn.bind("<Button-3>", self.right_click_actions) # convention in tkinter for the right click, we are only passing the reference of the function so no ()

        self.cell_btn_object = btn
    
    def left_click_actions(self, event): # add the event because it takes 2 positionnal arguments
        print(event)
        print("I am a left bitch!")

    def right_click_actions(self, event): # add the event because it takes 2 positionnal arguments
        print(event)
        print("I am right, bitch!")

    @staticmethod
def randomize_mines(): 
    # This function randomly assigns mines to 9 different cells

    picked_cells = random.sample( 
        # 'random.sample' is a method that returns a list of unique random elements.
        # It picks 9 unique cells from the 'Cell.all' collection.
        # 'Cell.all' is the list containing all the cells in the game.
        Cell.all, 9
    )
    
    # Now, for each cell selected by random.sample:
    for picked_cell in picked_cells:
        # Mark that cell as a mine by setting 'is_mine' to True
        picked_cell.is_mine = True


    def __repr__(self) :
        return f"Cell({self.x}, {self.y})" # friendly view of the object