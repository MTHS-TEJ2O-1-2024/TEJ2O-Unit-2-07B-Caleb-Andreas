"""
Created by: Mr. Coxall
Created on: Sep 2020
This module is a Micro:bit MicroPython program
"""

from microbit import *

# variables
cookieNumber = number = 0

# cookieNumber goes up by one on a button press.
while True:
    if button_a.is_pressed():
        cookieNumber = cookieNumber + 1
        display.clear()
        display.scroll(str(cokieNumber))

# reset cookieNumber
    if button_a.is_pressed():
        cookieNumber = 0
        display.clear()
        display.scroll(str(cokieNumber))
