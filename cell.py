from tkinter import Button


class Cell :
    def __init__(self, is_mine = False):
        self.is_mine = is_mine
        self.cell_btn_object = None
    
    def create_btn_object(self, location):
        btn = Button( # instance du bouton qui servira de cellule
            location, 
            text="bitch"
        )
        # BIND IS USED TO ASSOCIATE A EVENT TO A FUNCTION
        btn.bind("<Button-1>", self.left_click_actions) # convention in tkinter for the left click, we are only passing the reference of the function
        self.cell_btn_object = btn
    
    def left_click_actions(self, event): # add the event because it takes 2 positionnal arguments
        print(event)
        print("I am left bitch!")
