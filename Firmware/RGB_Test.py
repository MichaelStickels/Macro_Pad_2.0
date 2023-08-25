"""

  Macro_Keypad_2.0 RGB Functionality Tester

  Created by Michael Stickels

  GPL-3.0 License

"""


import board
import digitalio
from adafruit_debouncer import Debouncer
from rainbowio import colorwheel
import neopixel

pin = digitalio.DigitalInOut(board.D10)
pin.direction = digitalio.Direction.INPUT
pin.pull = digitalio.Pull.DOWN
switch = Debouncer(pin, interval = 0.1)

# Initialize RGB
pixel_pin = board.D3
num_pixels = 50
pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)

while True:
    switch.update()
    if switch.fell:
        print("Just released")
        pixels.fill((255,0,0))
        pixels.show
    if switch.rose:
        print("Just pressed")
        pixels.fill((0,0,255))
        pixels.show