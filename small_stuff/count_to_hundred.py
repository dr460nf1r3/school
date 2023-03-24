#!/usr/bin/env python

# Initial variable
i = 1 

# Do this while i is less than or equal to 100
while i <= 100:
    print(i)
    if i == 39:
        i = 61
        # Continue the while loop
        continue
    i += 1
