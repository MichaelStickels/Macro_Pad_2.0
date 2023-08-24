import time
import board
from analogio import AnalogIn

slider_pins = [AnalogIn(board.A9), AnalogIn(board.A8), AnalogIn(board.A7)]

coefficient = 1023 / 1023**2

def get_voltage(pin):
    return round(coefficient * pow(pin.value * 1023 / 65535 - 1023, 2))


while True:
    print_string = ""
    for pin in slider_pins:
        print_string += str(get_voltage(pin))
        if pin != slider_pins[-1]: print_string += "|"
    print(print_string)
    time.sleep(0.1)
