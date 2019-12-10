from .room_interface import Room

class Bedroom(Room):
    def __init__(self, context):
        self.context = context

    def enter_house(self):
        print("you are in the house")

    def leave_house(self):
        print("you are now outside the house")

    def enter_bedroom(self):
        print("you are now inside the bedroom")
        

    def leave_bedroom(self):
        print("you are outside the house")
        

    def enter_studyroom(self):
        print("you are now inside the studyroom")
        

    def leave_studyroom(self):
        print("you are outside the house")
        


