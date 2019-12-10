from .room_interface import Room

class OutsideHouse(Room):
    """ state you are in when you first begin the game"""
    def __init__(self, context):
        self.context = context
        self.collection_of_objects = ["mat", "door_to_house"]
        self.hidden_objects = ["key_under_mat"]
        self.files = {"key_under_mat" : "key_under_mat.txt"}

    def enter_house(self):
        self.context.state = self.context.in_house
        print("you have entered the house")

    def leave_house(self):
        print("you are outside the house")

    def enter_bedroom(self):
        print("you are outside the house")
        

    def leave_bedroom(self):
        print("you are outside the house")
        

    def enter_bedroom(self):
        print("you are outside the house")
        

    def enter_studyroom(self):
        print("you are outside the house")
        

    def leave_studyroom(self):
        print("you are outside the house")
        


