import board #adding "board" (allows for the board to be used)
import neopixel #adding "neopixel" (allows for the light to be used)
import time #adding "time" (allows for delays and such to be used)
R = 0 #Red value
G = 0 #Blue value
B = 255 #Green vlaue
var = 1 #Mode
delay = .01 #Delay (Raise to make it slower, lower to make it faster)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1) #light setup



while True:
    dot.fill((R,G,B)) #Turn the light the current set RGB values.
    print("mode", var) #Print to the serial monitor the current mode (Whether it's turning r, g, or b)
    print("R =",R) #Print the current R value top the serial monitor.
    print("G =",G) #Print the current B value top the serial monitor.
    print("B =", B) #Print the current G value top the serial monitor.
    if var == 1:
        R = R + 1 #Increase the R value by one.
        B = B - 1 #Decrease the B value by one.
        print("turning red") #Print to the serial monitor that it is turning red.
        time.sleep(delay) #Wait for however long the delay is.
        if R >= 255: #If the R value is equal to or greater than 255, make the mode 2 (Turning green)
            var = 2 # ^
    if var == 2:
        G = G + 1 #Increase the G value by one.
        R = R - 1 #Decrease the R value by one.
        print("turning green") #Print to the serial monitor that it is turning green.
        time.sleep(delay) #Wait for however long the delay is.
        if G >= 255: #If the G value is equal to or greater than 255, make the mode 3 (Turning blue)
            var = 3 # ^
    if var == 3:
        B = B + 1 #Increase the B value by one.
        G = G - 1 #Decrease the G value by one.
        print("turning blue") #Print to the serial monitor that it is turning blue.
        time.sleep(delay) #Wait for however long the delay is.
        if B >= 255: #If the B value is equal to or greater than 255, make the mode 1 (Turning red)
            var = 1 # ^