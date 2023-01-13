# Define our global variables & the dictionary holding our room name & sizes
all_rooms = {}
global wall_size
global room_size


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
    global wall_size
    wall_size = input(f"Please enter the {part} of the room: ")
    wall_size = float(wall_size)


# Calculate the actual room size
def calc_room_size():
    global room_size
    room_size = 0
    room_name = input("What is the name of this room? ")
    room_is_special = ask_yes_no("Does the room have special areas that need to be calculated additionally? ")

    # This is a normal room
    if not room_is_special:
        get_wall_size_normal("length")
        part_one = wall_size
        get_wall_size_normal("width")
        room_size = part_one * wall_size

    # This is a special room that needs several calculations
    while room_is_special:
        room_part_size = 0
        get_wall_size_normal("length of the part")
        part_one = wall_size
        get_wall_size_normal("width of the part")
        room_part_size = part_one * wall_size
        room_size += room_part_size

        # Break the loop if no more parts are to be added to the room_size
        room_is_special = ask_yes_no("Do we need to add additional parts? ")

    # Add the total room size to our dic
    all_rooms[room_name] = room_size
    print(f"This room is {all_rooms[room_name]} qm")


# Here the actual processing starts
room_counter_max = input("Please input how many rooms you would like to measure! ")
room_counter_max = int(room_counter_max)
rooms_measured = 1
print(f"Starting the calculation with room {rooms_measured}.")

# Calculate the room sizes until all rooms are done
while rooms_measured <= room_counter_max:
    calc_room_size()
    rooms_measured += 1
    print(f"Done with room {rooms_measured - 1}. Continuing with the next one.")

# Loop through the dictionary to calculate the total size
total_room_size = sum([room for room in all_rooms.values()])

print(
    ""
    f"These are all registered rooms:\n"
    f"{all_rooms}\n"
    f"The total size is {total_room_size}!"
)
