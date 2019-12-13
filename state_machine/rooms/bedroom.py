from .room_interface import Room

class Bedroom(Room):
    def __init__(self, context):
        self.context = context
        self.collection_of_objects = ["bed","table","chair","door_to_leave_bedroom"]
        self.hidden_objects = ["journal"]
        self.files = {"journal" : "journal.txt"}

    def enter_house(self):
        print("You are already in the house")

    def leave_house(self):
        print("You must first head into the livingroom in order to leave the house")

    def enter_bedroom(self):
        print("you are now inside the bedroom")
        

    def leave_bedroom(self):
        self.context.state = self.context.in_house
        print("you are now in the livingroom")
        

    def enter_studyroom(self):
        print("You must first head into the livingroom in order to enter the studyroom")
        

    def leave_studyroom(self):
        print("You can't as you are in the bedroom")
        


