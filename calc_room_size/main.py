"""A simple room size calculator that can handle a few different type of rooms."""
from datetime import datetime

# Initialize application
from functions import all_rooms, ask_yes_no, calc_room_size

# Here the actual processing starts
try:
    ROOM_COUNTER_MAX = int(input("Please input how many rooms you would like to measure! "))
except ValueError:
    print("This is not a valid number, assuming 1..")
    ROOM_COUNTER_MAX = 1
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
house_rent_price = total_room_size * float(input("What is the average rent for one qm? "))

print("These are all registered rooms:\n"
      f"{all_rooms}\n"
      f"Average room size: {average_room_size}.\n"
      f"Total room size  : {total_room_size}.\n"
      f"Estimated rent   : {house_rent_price} €\n")


# Offer saving the result to a file
def save_result_to_file():
    """Saves the complete result to a file."""
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y, %H:%M:")
    with open(str(input("Please enter the file path: ")), "a", encoding="UTF-8") as f:
        f.write(f"Room calculation results from {current_time}\n"
                "These are all registered rooms:\n"
                f"{all_rooms}\n"
                f"Average room size: {average_room_size}\n"
                f"Total room size  : {total_room_size}\n"
                f"Estimated rent   : {house_rent_price} €\n\n")
    f.close()


if ask_yes_no("Do you want to save the result to a file? "):
    while True:
        try:
            save_result_to_file()
            break
        except IOError as e:
            print("That is not a valid file path, try again..")
            continue

# We are done!
print("Done! ✅")
