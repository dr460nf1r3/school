# Initialize application
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

# Loop through the dictionary to calculate the total size
total_room_size = sum([room for room in all_rooms.values()])

# Our final output showing total size and all room stats
print(f"\nThese are all registered rooms:\n"
      f"{all_rooms}\n"
      f"The average room size is {total_room_size / room_counter_max}.\n"
      f"The total size is {total_room_size}!")
