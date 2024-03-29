"""A simple room size calculator that can handle a few different type of rooms."""
from datetime import datetime

# Initialize application
from functions import all_rooms, ask_yes_no, calc_room_size, bubblesort

# Get the amount of rooms to be dealt with. Also, we need to catch wrong
# input as exception.
ROOM_COUNTER_MAX = 0
while True:
    try:
        ROOM_COUNTER_MAX = int(
            input("Please input how many rooms you would like to measure! ")
        )
        if ROOM_COUNTER_MAX < 1:
            print("Are you sure about that? Select a number greater than 0!")
            continue
        if ROOM_COUNTER_MAX >= 1000:
            print("You crazy motherfucker, alright.")
        break
    except ValueError:
        print("This is not a valid number..")
        continue

# Starting the calculation with room 1
rooms_measured = 1  # pylint: disable=invalid-name
print(f"Starting the calculation with room {rooms_measured}.")

# Calculate the room sizes until all rooms are done
while rooms_measured <= ROOM_COUNTER_MAX:
    calc_room_size()
    if rooms_measured <= ROOM_COUNTER_MAX:
        print(f"Done with room {rooms_measured}. Continuing with the next one.\n")
    else:
        print("Finished calculating room sizes.\n")
    rooms_measured += 1

# Loop through the dictionary to calculate the total size
total_room_size = round(sum(list(all_rooms.values())), 2)

# Our final output showing total size and all room stats
average_room_size = round(total_room_size / ROOM_COUNTER_MAX, 2)
house_rent_price = total_room_size * float(
    input("What is the average rent in € for one m²? ")
)

print(
    "These are all registered rooms:\n"
    f"{all_rooms}\n"
    f"Average room size: {average_room_size} m²\n"
    f"Total room size  : {total_room_size} m²\n"
    f"Estimated rent   : {house_rent_price} €\n"
)


# Sort our dictionary by the room size
dict(sorted(all_rooms.items(), key=lambda item: item[1]))

# Print our now sorted dictionary
print(all_rooms)

# Implement a bubble sort algorithm to sort room sizes
room_list = list(all_rooms.values())
rooms_sorted = bubblesort(room_list)

# Print the sorted list
print(rooms_sorted)


# Offer saving the result to a file
def save_result_to_file():
    """Saves the complete result to a file."""
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y, %H:%M:")
    with open(
        str(input("Please enter the file path: ")), "a", encoding="UTF-8"
    ) as current_file:
        current_file.write(
            f"Room calculation results from {current_time}\n"
            "These are all registered rooms:\n"
            f"{all_rooms}\n"
            f"Average room size: {average_room_size} m²\n"
            f"Total room size  : {total_room_size} m²\n"
            f"Estimated rent   : {house_rent_price} €\n\n"
        )
    current_file.close()


if ask_yes_no("Do you want to save the result to a file? "):
    while True:
        try:
            save_result_to_file()
            break
        except IOError:
            print("That is not a valid file path, try again..")
            continue

# We are done!
print("Done! ✅")
