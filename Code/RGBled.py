import pulseio
import board
import time
class RGB:
    def __init__(self, pin1, pin2, pin3): #init sets up all of the given pins for PWMOut
        self.pin1 = pulseio.PWMOut(pin1, frequency=5000, duty_cycle=0)
        self.pin2 = pulseio.PWMOut(pin2, frequency=5000, duty_cycle=0)
        self.pin3 = pulseio.PWMOut(pin3, frequency=5000, duty_cycle=0)
    def red(self): #Turns the led red
        self.pin1.duty_cycle = 0    #Because of the kind of leds I have, I made the values opposite because the long pin is the positive pin.
        self.pin2.duty_cycle = 65535
        self.pin3.duty_cycle = 65535
    def blue(self): #Turns the led blue
        self.pin1.duty_cycle = 65535
        self.pin2.duty_cycle = 65535
        self.pin3.duty_cycle = 0
    def green(self): #Turns the led green
        self.pin1.duty_cycle = 65535
        self.pin2.duty_cycle = 0
        self.pin3.duty_cycle = 65535
    def magenta(self): #Turns the led magenta
        self.pin1.duty_cycle = 0
        self.pin2.duty_cycle = 65535
        self.pin3.duty_cycle = 0
    def yellow(self): #Turns the led yellow
        self.pin1.duty_cycle = 0
        self.pin2.duty_cycle = 0
        self.pin3.duty_cycle = 65535
    def rainbow(self, duration, speed): #Rainbow code that works off of a set duration and speed. (I fortunately had already made some code for a fading rainbow rgb led so I took it and edited it for PWN instead of the neopixel and added duration. Code: https://github.com/msweet53/CircuitPythonMAXS/blob/main/RainbowRGBEpicGamer.py)
        R = 0
        G = 0
        B = 255
        var = 1
        speed = .01
        self.duration = 0

        for x in range(duration * 100):
            self.pin1.duty_cycle = 65535 - R * 257 #convert the values to make it work with the PWM output and output them.
            self.pin2.duty_cycle = 65535 - B * 257
            self.pin3.duty_cycle = 65535 - G * 257
            if var == 1:
                R = R + 1 #Increase the R value by one.
                B = B - 1 #Decrease the B value by one.
                time.sleep(speed) #Wait for however long the delay is.
                if R >= 255: #If the R value is equal to or greater than 255, make the mode 2 (Turning green)
                    var = 2 # ^
            if var == 2:
                G = G + 1 #Increase the G value by one.
                R = R - 1 #Decrease the R value by one.
                time.sleep(speed) #Wait for however long the delay is.
                if G >= 255: #If the G value is equal to or greater than 255, make the mode 3 (Turning blue)
                    var = 3 # ^
            if var == 3:
                B = B + 1 #Increase the B value by one.
                G = G - 1 #Decrease the G value by one.
                time.sleep(speed) #Wait for however long the delay is.
                if B >= 255: #If the B value is equal to or greater than 255, make the mode 1 (Turning red)
                    var = 1 # ^
    def cyan(self): #Makes the led cyan
        self.pin1.duty_cycle = 65535
        self.pin2.duty_cycle = 0
        self.pin3.duty_cycle = 0
    def off(self): #Turns the led off
        self.pin1.duty_cycle = 65535
        self.pin2.duty_cycle = 65535
        self.pin3.duty_cycle = 65535

