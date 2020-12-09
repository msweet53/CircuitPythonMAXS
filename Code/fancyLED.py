from digitalio import DigitalInOut, Direction
import time
class FancyLED:
    def __init__(self, pin1, pin2, pin3):
        self.pin1 = DigitalInOut(pin1)
        self.pin2 = DigitalInOut(pin2)
        self.pin3 = DigitalInOut(pin3)
        self.pin1.direction = Direction.OUTPUT
        self.pin2.direction = Direction.OUTPUT
        self.pin3.direction = Direction.OUTPUT

    def alternate(self):
        self.pin1.value = True
        time.sleep(.5)
        self.pin1.value = False
        self.pin3.value = True
        time.sleep(.5)
        self.pin3.value = False
        self.pin2.value = True
        time.sleep(.5)
        self.pin2.value = False
    def blink(self):
        self.pin1.value = True
        self.pin2.value = True
        self.pin3.value = True
        time.sleep(.5)
        self.pin1.value = False
        self.pin2.value = False
        self.pin3.value = False
        time.sleep(.5)
    def chase(self):
        self.pin1.value = True
        time.sleep(.5)
        self.pin1.value = False
        self.pin2.value = True
        time.sleep(.5)
        self.pin2.value = False
        self.pin3.value = True
        time.sleep(.5)
        self.pin3.value = False
    def sparkle(self):
        self.pin1.value = True
        time.sleep(.1)
        self.pin1.value = False
        time.sleep(.1)
        self.pin3.value = True
        time.sleep(.1)
        self.pin3.value = False
        time.sleep(.1)
        self.pin2.value = True
        time.sleep(.1)
        self.pin2.value = False
        time.sleep(.1)

