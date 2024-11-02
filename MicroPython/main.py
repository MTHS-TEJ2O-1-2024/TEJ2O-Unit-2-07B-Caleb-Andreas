"""
Created by: Caleb Andreas
Created on: Nov 2024
This module is a Micro:bit MicroPython program that is a cookie clicker.
"""

from microbit import *


# Variables.
cookieNumber = number = 0

# Happy face at start.
display.clear()
display.show(Image.HAPPY)

# cookieNumber goes up by one on a button press.
while True:
    if button_a.is_pressed():
        cookieNumber = cookieNumber + 1
        display.clear()
        display.show(str(cookieNumber))

    # Reset cookieNumber on b button press.
    if button_b.is_pressed():
        cookieNumber = 0
        display.clear()
        display.show(str(cookieNumber))
