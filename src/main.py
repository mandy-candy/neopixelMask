# main.py

from machine import Pin
import neopixel

# one ring has 16 pixels
pixel = neopixel.NeoPixel(Pin(5), 32)
# get number of pixels out of object
index = pixel.n


for i in range(index):
    pixel[i] = (10, 0, 0)
    pixel.write()  