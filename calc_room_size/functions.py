"""This module contains all the necessary functions to do our calculations."""

# To do circle calculations
import math

# Initialize our dictionary
all_rooms = {}


def ask_yes_no(query):
    """Ask a simple yes/no question and return True/False."""
    yes_choices = ["yes", "y", "j", "ja"]
    no_choices = ["no", "n", "nein"]

    while True:
        user_input = input(query)
        if user_input.lower() in yes_choices:
            return True
        if user_input.lower() in no_choices:
            return False
        print("Only yes or no are valid answers! Try again.")


def get_room_type():
    """Get the type of room that is being measured."""
    normal_room_choices = ["normal", "1", "1."]
    special_room_choices = ["special", "2", "2."]
    roof_room_choices = ["roof", "3", "3."]
    circle_room_choices = ["circle", "4", "4."]
    segment_room_choices = ["segment", "5", "5."]

    while True:
        user_input = input("What kind of room are we going to calculate the size for?\n"
                           "1. A normal room\n"
                           "2. A room with multiple square parts\n"
                           "3. A room with roof tiles\n"
                           "4. A room which is a circle\n"
                           "5. A room which is a circle segment\n"
                           "Enter the number or type of the room: ")

        if user_input.lower() in normal_room_choices:
            return "normal"
        if user_input.lower() in special_room_choices:
            return "special"
        if user_input.lower() in roof_room_choices:
            return "roof"
        if user_input.lower() in circle_room_choices:
            return "circle"
        if user_input.lower() in segment_room_choices:
            return "segment"
        print('This is not a valid answer! Try again.')


# Get the wall size and convert it to a float
def get_wall_size_normal(part):
    """Input the wall size and return the floated value"""
    wall_size = float(input(f"Please enter the {part} of the room: "))
    return wall_size


def calc_room_size():
    """Calculate the actual room size depending on the room type."""
    room_size = 0
    room_name = input("What is the name of this room? ")
    room_type = get_room_type()

    if room_type == "normal":
        # This is a normal room
        room_size += get_wall_size_normal("length") * \
                     get_wall_size_normal("width")
    if room_type == "special":
        # This is a special room that needs several calculations
        while True:
            room_size += get_wall_size_normal("length of the part") * \
                         get_wall_size_normal("width of the part")
            # Break the loop if no more parts are to be added to the room_size
            if not ask_yes_no("Do we need to add additional parts? "):
                break
    if room_type == "roof":
        # This has a roof tile that needs to be calculated differently
        room_size = (get_wall_size_normal("length") *
                     get_wall_size_normal("width")) / 2
    if room_type == "circle":
        room_size = round(
            (math.pow(float(input("Please enter the radius of the room: ")), 2) * math.pi), 2)
    if room_type == "segment":
        segment_radius = float(
            input("Please enter the radius of the segment: "))
        segment_angle = float(
            input("Please enter the angle of the segment: "))
        room_size = (math.pi * (segment_radius * segment_radius) *
                     (segment_angle / 360)) - (1 / 2 * (segment_radius * segment_radius) *
                                               math.sin((segment_angle * math.pi) / 180))

    # Add the total room size to our dictionary
    all_rooms[room_name] = room_size
    print(f"This room is {all_rooms[room_name]} qm")
