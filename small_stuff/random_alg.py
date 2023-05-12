#!/usr/bin/env python

y = 1
x = int(input("Enter a number: "))
not_done = True

while not_done:
    if x > 0:
        y = y * x
        x = x - 1
    elif x == 0:
        if y > 0:
            print(y)
            not_done = False
        else:
            y = -y
    else:
        y = y * x
        x = x + 1
