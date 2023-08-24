"""

  Macro_Keypad_2.0 Firmware

  Created by Michael Stickels
  
  Last Updated: *#*#*#*#

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

# Imports
import time
import board
from analogio import AnalogIn


# Deej setup
slider_pins = [AnalogIn(board.A9), AnalogIn(board.A8), AnalogIn(board.A7)]
coefficient = 1023 / 1023**2




# Deej Helper
def get_voltage(pin):
    return round(coefficient * pow(pin.value * 1023 / 65535 - 1023, 2))



# Loop
while True:

    # Build and send Deej string
    print_string = ""
    for pin in slider_pins:
        print_string += str(get_voltage(pin))
        if pin != slider_pins[-1]: print_string += "|"  # Append | only between slider values for Deej
    print(print_string)
    
    
    # Delay
    time.sleep(0.1)
