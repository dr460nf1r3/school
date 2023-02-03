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


def get_room_type():
    normal_room_choices = ['normal', '1', '1.']
    special_room_choices = ['special', '2', '2.']
    roof_room_choices = ['roof', '3', '3.']

    while True:
        user_input = input("What kind of room are we going to calculate the size for?\n"
                           "1. a normal room\n"
                           "2. a room with multiple square parts\n"
                           "3. a room with roof tiles\n"
                           "Enter the number or type of the room: ")

        if user_input.lower() in normal_room_choices:
            return "normal"
        elif user_input.lower() in special_room_choices:
            return "special"
        elif user_input.lower() in roof_room_choices:
            return "roof"
        else:
            print('This is not a valid answer! Try again.')


# Get the wall size and convert it to a float
def get_wall_size_normal(part):
    wall_size = float(input(f"Please enter the {part} of the room: "))
    return wall_size


# Calculate the actual room size
def calc_room_size():
    room_size = 0
    room_name = input("What is the name of this room? ")
    room_type = get_room_type()

    if room_type == "normal":
        # This is a normal room
        room_size += get_wall_size_normal("length") * get_wall_size_normal("width")
    elif room_type == "special":
        # This is a special room that needs several calculations
        lets_loop_wall_size = True
        while lets_loop_wall_size:
            room_size += get_wall_size_normal("length of the part") * get_wall_size_normal("width of the part")
            # Break the loop if no more parts are to be added to the room_size
            if not ask_yes_no("Do we need to add additional parts? "):
                lets_loop_wall_size = False
    elif room_type == "roof":
        # This has a roof tile that needs to be calculated differently
        room_size = (get_wall_size_normal("length") * get_wall_size_normal("width")) / 2

    # Add the total room size to our dictionary
    all_rooms[room_name] = room_size
    print(f"This room is {all_rooms[room_name]} qm")


# Here the actual processing starts
room_counter_max = int(input("Please input how many rooms you would like to measure! "))
rooms_measured = 1
print(f"Starting the calculation with room {rooms_measured}.")

# Calculate the room sizes until all rooms are done
while rooms_measured <= room_counter_max:
    calc_room_size()
    if (rooms_measured + 1) <= room_counter_max:
        print(f"Done with room {rooms_measured}. Continuing with the next one.\n")
    rooms_measured += 1

# Loop through the dictionary to calculate the total size
total_room_size = sum([room for room in all_rooms.values()])

print(f"\nThese are all registered rooms:\n"
      f"{all_rooms}\n"
      f"The average room size is {total_room_size / room_counter_max}.\n"
      f"The total size is {total_room_size}!")
