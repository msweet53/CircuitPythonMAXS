import time
import board
import pulseio
import servo
import touchio
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50) #sets PWM for servo

servoang = 90 #Base servo angle

my_servo = servo.Servo(pwm) #servo setup
touch_padPOS = board.A0 #cap touch setup (setting pins)
touch_padNEG = board.A1 #cap touch setup (setting pins)
touchPOS = touchio.TouchIn(touch_padPOS) #cap touch setup (setting input/output)
touchNEG = touchio.TouchIn(touch_padNEG) #cap touch setup (setting input/output)
while True:
    if touchPOS.value: #if neg wire is touched:
        print("neg trigger") #prints it was touched
        servoang = servoang - 1 #subtracts from servo angle
        time.sleep(.01) #small delay (change to change speed of servo)
    if touchNEG.value: #if pos wire is touched:
        print("pos trigger") #prints it was touched
        servoang = servoang + 1 #adds to servo angle
        time.sleep(.01) #small delay (change to change the speed of servo)
    my_servo.angle = servoang #updates servo
    print(servoang) #prints current angle of servo
    if servoang > 179: #checks to see if servo is maxing positive
        print("POS max") #prints that it maxed
        servoang = 178 #sets servo angle to just below max
        time.sleep(.5) #delay
    if servoang < 1: #checks to see if servo is maxxing negative
        print("NEG max") #prints that it maxed
        servoang = 2 #sets servo angle just above the minimum
        time.sleep(.5) #delay