import digitalio #imports your boards IO
from board import * #honestly dont know but import board wouldn't work but this did.
import time #lets you use the delay feature and stuff.
delay = 1 #change to change speed of blink.

led = digitalio.DigitalInOut(D13) #sets led to pin 13
led.direction = digitalio.Direction.OUTPUT #sets led to an output
while True:
    led.value = True #turns on
    time.sleep(delay) #delay
    led.value = False #turns off
    time.sleep(delay) #delay