# Define our global variables & the dictionary holding our room name & sizes
all_rooms = {}


# We need to ask for this multiple times, therefore we make it a function
def ask_yes_no(query):
    yes_choices = ['yes', 'y', 'j', 'ja']
    no_choices = ['no', 'n', 'nein']

    while True:
        user_input = input(query)
        if user_input.lower() in yes_choices:
            return True
        elif user_input.lower() in no_choices:
            return False
        else:
            print('Only yes or no are valid answers! Try again.')


# Get the wall size and convert it to a float
def get_wall_size_normal(part):
    wall_size = float(input(f"Please enter the {part} of the room: "))
    return wall_size


# Calculate the actual room size
def calc_room_size():
    room_size = 0
    room_name = input("What is the name of this room? ")
    room_is_special = ask_yes_no("Does the room have special areas that need to be calculated additionally? ")

    # This is a normal room
    if not room_is_special:
        room_size += get_wall_size_normal("length") * get_wall_size_normal("width")

    # This is a special room that needs several calculations
    while room_is_special:
        room_size += get_wall_size_normal("length of the part") * get_wall_size_normal("width of the part")

        # Break the loop if no more parts are to be added to the room_size
        room_is_special = ask_yes_no("Do we need to add additional parts? ")

    # Add the total room size to our dic
    all_rooms[room_name] = room_size
    print(f"This room is {all_rooms[room_name]} qm")


# Here the actual processing starts
room_counter_max = int(input("Please input how many rooms you would like to measure! "))
rooms_measured = 1
print(f"Starting the calculation with room {rooms_measured}.")

# Calculate the room sizes until all rooms are done
while rooms_measured <= room_counter_max:
    calc_room_size()
    print(f"Done with room {rooms_measured}. Continuing with the next one.")
    rooms_measured += 1

# Loop through the dictionary to calculate the total size
total_room_size = sum([room for room in all_rooms.values()])

print(""
      f"These are all registered rooms:\n"
      f"{all_rooms}\n"
      f"The total size is {total_room_size}!")
