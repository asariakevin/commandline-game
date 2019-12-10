class Room:

    def __init__(self):
        self.collection_of_objects = []
        self.hidden_objects = []
        self.files = {}


    # ls command
    def print_collection_of_objects(self):
        for object_in_room in self.collection_of_objects:
            print(object_in_room)

    # ls -a 
    def print_even_hidden_objects(self):
        self.print_collection_of_objects()

        for hidden_object in self.hidden_objects:
            print(hidden_object)

    # cd directory
    def change_room(room):

        if room is not "..":
            enter_room()

        else:
            leave_room()

    # cat and less  file
    def display_file(self,filename):
        with open(self.files[filename]) as f:
           print( f.read())

    # grep file
    def display_greped_file(self,filename, pattern):
        pass

    def enter_house(self):
        " function called to change state"
        pass

    def leave_house(self):
        pass

    def enter_bedroom(self):
        pass

    def leave_bedroom(self):
        pass

    def enter_bedroom(self):
        pass

    def enter_studyroom(self):
        pass

    def leave_studyroom(self):
        pass

    


