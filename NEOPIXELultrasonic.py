import time #general library setup
import board
import adafruit_hcsr04 #ultrasonic library
import neopixel #neopixel library

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D6) #ultrasonic variable setup
dot = neopixel.NeoPixel(board.NEOPIXEL, 1) #neopixel variable setup

R = 0 # R, G, and B vars.
G = 0
B = 0


while True:
    try:
        print("Distance:", str(sonar.distance)) #prints to serial monitor the distance
        print("R=", R) #prints to serial monitor the R value
        print("G=", G) #prints to serial monitor the G value
        print("B=", B) #prints to serial monitor the B value
        dot.fill((R,G,B)) #makes the led light up with the R, G, and B variables.
        R = -17 * sonar.distance +  342.5 #equation for green transition
        G = 17 * sonar.distance -  342.5 #equation for green transition
        B = -17 * abs(sonar.distance - 20.147) + 255 #equation for blue transition
        if R <= 0 or R > 255: #all 3 of these insure that the color values dont go past their minimums and maximums
            R = 0
        if G <= 0 or G > 255:
            G = 0
        if B <= 0 or B > 255:
            B = 0
    except RuntimeError: #common error, here so it doesnt stop the code and you have to reset
        print("Retrying!") #print "retrying"
    time.sleep(.1) #delay maximizes smoothness and performace and minimizes errors