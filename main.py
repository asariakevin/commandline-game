from state_machine.state_machine import StateMachine
import utils

regular_user_prompt = "$ "
super_user_prompt = "# "
state_machine = StateMachine()

print(utils.beginning_message)
print()
print()


def user_choice(choice):

    if choice == "cd door_to_house":
        
        state_machine.enter_house()

    elif choice == "cd door_to_outside_house":
        
        state_machine.leave_house()
    elif choice == "cd door_to_bedroom":
        
        state_machine.enter_bedroom()

    elif choice == "cd door_to_leave_bedroom":
        
        state_machine.leave_bedroom()

    elif choice == "cd door_to_studyroom":
        
        state_machine.enter_studyroom()
    elif choice == "cd door_to_leave_studyroom":
        
        state_machine.leave_studyroom()

    elif choice == "ls":
        
        state_machine.print_collection_of_objects()

    elif choice == "ls -a":
        state_machine.print_even_hidden_objects()

    elif choice == "cat":
        state_machine.display_file("key_under_mat")

    else:
        print("I didn't get your command")


def playgame():
    print()
    print()
    print(utils.choosen_mission_message)
    
    while True:
        user_input = input(regular_user_prompt)
        user_choice(user_input)

accept_mission = input(utils.question_message)

if accept_mission == "y" or "yes":
    playgame()

elif accept_mission == "n" or "no":
    print("try")


