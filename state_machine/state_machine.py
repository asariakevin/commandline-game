from .rooms.in_house import InHouse
from .rooms.outside_house import OutsideHouse
from .rooms.bedroom import Bedroom

class StateMachine:
    """ This class holds the whole state machine"""

    def __init__(self):

        self.outside_house = OutsideHouse(self)
        self.in_house = InHouse(self)
        self.bedroom = Bedroom(self)
        self.state = self.outside_house

    def enter_house(self):
        self.state.enter_house()

    def leave_house(self):
        self.state.leave_house()

    def enter_bedroom(self):
        self.state.enter_bedroom()

    def leave_bedroom(self):
        self.state.leave_bedroom()


    def enter_studyroom(self):
        self.state.enter_studyroom()

    def leave_studyroom(self):
        self.state.leave_studyroom()

    # ls command
    def print_collection_of_objects(self):
        self.state.print_collection_of_objects()

    # ls -a 
    def print_even_hidden_objects(self):
        self.state.print_even_hidden_objects()

    # cd directory
  #  def change_room(room):

  #      if room is not "..":
  #          enter_room()

  #      else:
  #          leave_room()

    # cat and less  file
    def display_file(self,filename):
        self.state.display_file(filename)
    # grep file
    def display_greped_file(self,filename, pattern):
        pass



    
