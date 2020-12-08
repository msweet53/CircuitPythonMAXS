import board #board setup
import time #board setup
import pulseio #cap touch setup
import touchio #cap touch setup
from lcd.lcd import LCD #lcd setup
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface #lcd setup
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16) #lcd setup

direction = True #bool for counter direction
counter = 0 #int for counter
addsub = 1 #int for amount to add to counter

lcd.clear() #clers lcd screen
touch_padTOG = board.A0 #cap touch pin setup
touch_padCOUNT = board.A1 #cap touch pin setup
touchTOG = touchio.TouchIn(touch_padTOG) #cap touch input setup
touchCOUNT = touchio.TouchIn(touch_padCOUNT) #cap touch input setup

while True:
    if touchTOG.value:  #if toggle wire is touched:
        direction = not direction   #flip direction bool
        print("tog touched")    #print "tog touched" to serial monitor
        while touchTOG.value:   #prevents changing multiple times while held down
            pass    #Pass does nothing, just makes it kinda sit there.
    if direction == True:   #If the direction bool is true:
        addsub = 1  #make the amount added to the counter positive 1
        lcd.set_cursor_pos(0,0) #Set the lcd cursor to the top row
        lcd.print("Direction: Up  ")    #Print "Direction: Up  " to lcd. (reason for spaces is to clear the 4 character word "down" aswell)
    else:   #if the direction bool isn't true (false):
        addsub = -1 #make the amount added to the counter negative 1
        lcd.set_cursor_pos(0,0) #Set the lcd cursor to the top row
        lcd.print("Direction: Down")    #Print "Direction: Down"
    if touchCOUNT.value:    #if the counter wire is touched:
        print("counter touched")    #print "counter touched" to lcd screen
        counter = counter + addsub  #add the amount added variable to the counter
        while touchCOUNT.value: #Prevents adding multiple times while held down
            pass    #pass does nothing, just makes it kinda sit there.
    if counter == 0: #all of this if statement prevents the lcd screen from keeping characters when it isn't supposed to (when it goes negative since there are 2 characters it likes to keep the second one and it looks like the counter says "11" when it's supposed to say "1"
        lcd.set_cursor_pos(1,0)
        lcd.print("        ")
    lcd.set_cursor_pos(1,0) #set the lcd cursor to the bottom row
    lcd.print(str(counter)) #print the counter to the lcd (reason for str() function is so that it turns the counter into a string because for some reason the lcd library doesn't print integers)