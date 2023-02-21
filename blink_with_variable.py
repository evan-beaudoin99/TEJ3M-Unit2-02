import time
import board
from digitalio import DigitalInOut, Direction


# LED setup for onboard LED
led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

blink_time = 1

while True:

    led.value = True
    print("led on")
    time.sleep(blink_time)

    led.value = False
    print("led off")
    time.sleep(1)
    
    blink_time += 1
