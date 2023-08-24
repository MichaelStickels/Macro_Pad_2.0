"""

  Macro_Keypad_2.0 Keypad Functionality Tester

  Created by Michael Stickels

  GPL-3.0 License


Seeeduino XIAO pin assignments:
    D0  - Keypad row 3
    D1  - Keypad row 2
    D2  - Keypad row 1
    D3  - DRGB LED
    D4  - Keypad column 1
    D5  - Keypad column 2
    D6  - Keypad column 3
    A7  - Slider pot 3
    A8  - Slider pot 2
    A9  - Slider pot 1
    D10 - Button
  

"""

import keypad
import board

km = keypad.KeyMatrix(
    row_pins=(board.D2, board.D1, board.D0),
    column_pins=(board.D4, board.D5, board.D6),
)

while True:
    event = km.events.get()
    if event:
        print(event)
