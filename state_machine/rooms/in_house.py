from .room_interface import Room

class InHouse(Room):
    def __init__(self, context):
        self.context = context
        self.collection_of_objects = ["pic_of_root", "door_to_bedroom","door_to_studyroom","door_to_kitchen"]
        self.hidden_objects = []
        self.files = {}

    def enter_house(self):
        print("you are in the house")

    def leave_house(self):
        self.context.state = self.context.outside_house
        print("you are now outside the house")

    def enter_bedroom(self):
        self.context.state = self.context.bedroom
        print("you are now inside the bedroom")
        

    def leave_bedroom(self):
        print("you are outside the house")
        

    def enter_studyroom(self):
        context.state = context.studyroom
        print("you are now inside the studyroom")
        

    def leave_studyroom(self):
        print("you are outside the house")
        


