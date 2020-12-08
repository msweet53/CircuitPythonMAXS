import board #board setup
import time #board setup
import digitalio #board setup
from digitalio import DigitalInOut, Direction, Pull #Imports things necessary for I/O
from lcd.lcd import LCD #lcd setup
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface #lcd setup
lcd = LCD(I2CPCF8574Interface(0x27), num_rows=2, num_cols=16) #lcd setup


interrupter = DigitalInOut(board.D6) #sets photointerrupter pin to 6
interrupter.direction = Direction.INPUT #sets as input
interrupter.pull = Pull.UP #sets as pullup
lcd.clear() #clears lcd screen

hitamount = 0 #counter for hits
firstdelay = 4 #Change both of these values to change the refreash rate delay
totaldelay = 4
while True:
    lcd.set_cursor_pos(0,0) #Sets lcd cursor to top row
    lcd.print("Times hit:") #Prints "Times hit:" on top row
    if interrupter.value: #if the photointerrupter is hit
        print("hit") #Print "hit" to the serial monitor
        hitamount += 1 #Adds to the total hit count
        while interrupter.value: #This prevents it from counting multiple times for one hit.
            pass
    Remaining = firstdelay - time.time() #Makes the time remaining until it refreshes your set delay - the time the board has been on.
    if Remaining <= 0: #If remaining is equal to or less than 0:
        print("Time reset") #Print "Time reset" to serial monitor.
        lcd.set_cursor_pos(1,0) #Set lcd cursor to bottom row.
        lcd.print(str(hitamount)) #print the hit amount to the lcd bottom row
        firstdelay = time.time() + totaldelay #sets the time until it resfreshes the count the time the board has been on plus the same value as the original delay (in this case 4)

