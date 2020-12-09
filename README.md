# CircuitPythonMAXS
## PLEASE NOTE:
The board I used for these assignments is a Metro Express M0. NOT an Arduino Uno RC3. Some things Needed to be subsituted in the circuit diagrams sush as: Arduino Uno for Metro Express M0, 8 pin header for loose wire, and a random sensor for the Photointerruptor. Please also take into account that I used an lcd backpack with my lcd screen. So the shown wiring is very incorrect.
## Circuit Python assignment 1
[RainbowRGBEpicGamer.py](https://github.com/msweet53/CircuitPythonMAXS/blob/main/Code/RainbowRGBEpicGamer.py)
### Desc.
This code makes it so that the neopixel on the metro express fades between the colors on the RGB spectrum at a variable rate.
### Lessons learned:
I learned that in circuit python to change a variable through addition or subraction you could not just put something like R - 1. You would have to put something like R = R - 1.
### Pictures/GIFs
![](GIFs/RGBepicgamerGIF.gif)
## Circuit Python assignment 2
[LEDBlink.py](https://github.com/msweet53/CircuitPythonMAXS/blob/main/Code/LEDBlink.py)
### Desc.
This code makes it so that a LED wired to digital pin 13 blinks at a variable rate.
### Lessons learned.
I learned that you have to determine whether your pin is an output or an input.
### Pictures/GIFs
![](LEDBlinkGIF.gif)
## Circuit Python assignment 3
[CAPtouchSERVO.py](https://github.com/msweet53/CircuitPythonMAXS/blob/main/Code/CAPtouchSERVO.py)
### Desc.
This code makes it so that when you touch one of the wires, the servo moves in one direction, then when you touch the other wire it moves in the opposite direction.
### Lessons Learned:
That when the servo goes over 180 or under 0, it comes back as an error so you have to code to prevent that.
### Pictures/GIFs
![](CAPtouchSERVOGIF.gif)
## Circuit Python assignment 4
[CAPtouchLCD.py](https://github.com/msweet53/CircuitPythonMAXS/blob/main/Code/CAPtouchLCD.py)
### Desc.
This makes it so that when you touch one wire the mode changes from up to down or from down to up, then when you touch the other wire the counter will either go up or down depending on which mode it is on, all displayed real time on an lcd screen.
### Lessons Learned:
I learned that with the lcd backpack library for circuit python, the lcd.print() funtion does not work with integers, and you have to turn the integer you want to display into a string with the str() function first.
### Pictures/GIFs
![](CAPtouchLCDGIF.gif)
## Circuit Python Assignment 4
[PHOTOINTERRUPTERlcdcount.py](https://github.com/msweet53/CircuitPythonMAXS/blob/main/Code/PHOTOINTERRUPTERlcdcount.py)
### Desc.
Code so that when you interrupt a photo interrupter, it adds to a counter that refreshes every 4 seconds.
### Lessons Learned:
Doing that without using the sleep() funtion was very difficult.
### Pictures/GIFs
![](PHOTOINTERRUPTERlcdcountGIF.gif)
## Circuit Python assignment 5
[NEOPIXELultrasonic.py](https://github.com/msweet53/CircuitPythonMAXS/blob/main/Code/NEOPIXELultrasonic.py)
### Desc.
In this code, the onboard neopixel of a metro express M0 fades between the colors on the rgb spectrum based on how far away an object is from an ultrasonic sensor.
### Lessons Learned:
With the library for circuit python with the ultrasonic sensor, it has this annoying error that will just stop your code entirely if you haven't coded around it being able to stop your code entirely. Also if you get the error the neopixel turns like a bright green.
### Pictures/ GIFs
![](ULTRASONICneopixelGIF.gif)
## Circuit Python assignment 6
[RGBled.py](https://github.com/msweet53/CircuitPythonMAXS/blob/main/Code/RGBled.py)
### Desc.
A class that allows a 4 pin rgb led to be comtrolled easily with multiple varying functions.
### Lessons learned:
I learned that it is very easy to have something get stuck in a loop and have your code just do that one loop instead of going on with the rest of your code. I was having a problem with the rgb fade module and it would just get stuck there. So I had to make it so that you could set a duration for it to last. 
### Pictures/GIFs
![](RGBledGIF.gif)
## Circuit Python assignment 7
[fancyLED.py](https://github.com/msweet53/CircuitPythonMAXS/blob/main/Code/fancyLED.py)
### Desc.
A class code to be used with code provided with the assignment. (Code provided is multiple functions that you need to make with modules and classes in your other code)
### Lessons learned:
I learned how to make a class and a module and how to make them work with digital IO. (Learned this because I was unable to do the previous assignment before this one due to not having to correct type of LED)
### Pictures/GIFs:
![](fancyLEDGIF.gif)
