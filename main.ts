/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: Caleb Andreas
 * Created on: Oct 2024
 * This program is a clicker game.
*/

//Define variable
let cookieNumber = 0

// Happy face at start
basic.clearScreen()
basic.showIcon(IconNames.Happy)

// cookieNumber goes up by 1 when A button pressed
input.onButtonPressed(Button.A, function() {
    basic.clearScreen()
    cookieNumber = cookieNumber + 1
    basic.showNumber(cookieNumber)
})

// Reset cookieNumber when B button is pressed.
input.onButtonPressed(Button.B, function () {
    basic.clearScreen()
    cookieNumber = 0
    basic.showNumber(cookieNumber)
})
