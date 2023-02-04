# Initialize application
from datetime import datetime

from functions import *

# Here the actual processing starts
room_counter_max = int(input("Please input how many rooms you would like to measure! "))
rooms_measured = 1
print(f"Starting the calculation with room {rooms_measured}.")

# Calculate the room sizes until all rooms are done
while rooms_measured <= room_counter_max:
    calc_room_size()
    rooms_measured += 1
    if rooms_measured <= room_counter_max:
        print(f"Done with room {rooms_measured}. Continuing with the next one.\n")
    else:
        print(f"Finished calculating room sizes.\n")
# Loop through the dictionary to calculate the total size
total_room_size = round(sum([room for room in all_rooms.values()]), 2)

# Our final output showing total size and all room stats
average_room_size = round(total_room_size / room_counter_max, 2)
print(f"These are all registered rooms:\n"
      f"{all_rooms}\n"
      f"Average room size: {average_room_size}.\n"
      f"Total room size  : {total_room_size}.\n")

# Offer saving the result to a file
if ask_yes_no("Do you want to save the result to a file? "):
    now = datetime.now()
    current_time = now.strftime("%m/%d/%Y, %H:%M:")
    f = open(str(input("Please enter the file path: ")), "a")
    f.write(f"Room calculation results from {current_time}\n"
            f"These are all registered rooms:\n"
            f"{all_rooms}\n"
            f"Average room size: {average_room_size}\n"
            f"Total room size  : {total_room_size}\n\n")
    f.close()
    print("Done! ✅")
