#requires circuitpython 7.3 or greater, and the NeoPixel library from Adafruit
#https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/rgb.md
#idk what im doin
print("Starting")

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RBG

import board

rgb = RGB(pixel_pin=board.SDA, num_pixels=2)
keyboard.extensions.append(led)

keyboard = KMKKeyboard()

keyboard.col_pins = (board.MOSI, board.MISO, board.SCK)
keyboard.row_pins = (board.RX)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [KC.Z, KC.X, KC.C]
]

if __name__ == '__main__':
    keyboard.go()
