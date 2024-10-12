from tkinter import Button
import random # library that gives random object
import settings

class Cell :
    all = []
    def __init__(self, x, y, is_mine = False): # passing x and y to define position
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
    
    
    # Append the object to the Cell.all list (= array)
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button( # instance du bouton qui servira de cellule
            location, 
            width =12, 
            height=4
        )
        # BIND IS USED TO ASSOCIATE A EVENT TO A FUNCTION
        btn.bind("<Button-1>", self.left_click_actions) # convention in tkinter for the left click, we are only passing the reference of the function so no ()
        btn.bind("<Button-3>", self.right_click_actions) # convention in tkinter for the right click, we are only passing the reference of the function so no ()

        self.cell_btn_object = btn
    
    def left_click_actions(self, event): # event added because it takes 2 positionnal arguments
        if self.is_mine: # if it is true 
            self.show_mine() 
        else : 
            self.show_cell()

    def get_cell_by_axis(self, x, y):
        # This method retrieves a cell object from the 'Cell.all' list
        # based on the provided coordinates (x, y). 
        for cell in Cell.all:
            # Loop through all the cells in the 'Cell.all' list.
            if cell.x == x and cell.y == y:
                # Check if the current cell's coordinates match the given x and y.
                return cell  # If a match is found, return that cell object.

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
            ]
        cells = [cell for cell in cells if cell is not None]
        return cells
    

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        
        return counter


    def show_cell(self): # checks all the cells around
        self.cell_btn_object.configure(text = self.surrounded_cells_mines_length)
        #print(f"({self.surrounded_cells_mines_length})")

        

    def show_mine(self):
        # A logic to interrupt the game and display a message that player lost
        self.cell_btn_object.configure(bg="red")


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
            Cell.all, settings.MINES_COUNT
        )
        
        # Now, for each cell selected by random.sample:
        for picked_cell in picked_cells:
            # Mark that cell as a mine by setting 'is_mine' to True
            picked_cell.is_mine = True

        def __repr__(self) :
            return f"Cell({self.x}, {self.y})" # friendly view of the object