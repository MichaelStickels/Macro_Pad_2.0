import time
import board
from rainbowio import colorwheel
import neopixel

pixel_pin = board.D3
num_pixels = 50

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.01, auto_write=False)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            rc_index = (i * 256 // num_pixels) + j
            pixels[i] = colorwheel(rc_index & 255)
        pixels.show()
        time.sleep(wait)


RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)

while True:
    rainbow_cycle(0)  # Increase the number to slow down the rainbow