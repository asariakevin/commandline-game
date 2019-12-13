from .room_interface import Room

class StudyRoom(Room):
    def __init__(self, context):
        self.context = context
        self.collection_of_objects = ["the_logic_machine","table","chair","door_to_leave_studyroom","the_greatest_story_ever_told"]
        self.hidden_objects = ["the_book_of_random_numbers"]
        self.files = {"the_book_of_random_numbers" : "the_book_of_random_numbers.txt"}

    def enter_house(self):
        print("You are already in the house")

    def leave_house(self):
        print("You must first head into the livingroom in order to leave the house")

    def enter_bedroom(self):
        print("You must first head into the livingroom in order to enter the bedroom")
        

    def leave_bedroom(self):
       pass 

    def enter_studyroom(self):
        self.context.state = self.context.studyroom
        print("You are now in the studyroom")

    def leave_studyroom(self):
        self.context.state = self.context.in_house
        print("You are now in the livingroom")
        


