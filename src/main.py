# main.py

from machine import Pin
import neopixel

# one ring has 16 pixels
pixel = neopixel.NeoPixel(Pin(5), 32)
# get number of pixels out of object
index = pixel.n


def ring(startLed, red, green, blue):
    for i in range(startLed, startLed + 16):
        pixel[i] = (red, green, blue)
        pixel.write()


ring(0, 10, 0, 0)
ring(16, 10, 0, 10)