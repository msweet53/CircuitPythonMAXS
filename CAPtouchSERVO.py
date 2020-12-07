import time
import board
import pulseio
import servo
import touchio
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

servoang = 90

my_servo = servo.Servo(pwm)
touch_padPOS = board.A0
touch_padNEG = board.A1
touchPOS = touchio.TouchIn(touch_padPOS)
touchNEG = touchio.TouchIn(touch_padNEG)
while True:
    if touchPOS.value:
        print("neg trigger")
        servoang = servoang - 1
        time.sleep(.01)
    if touchNEG.value:
        print("pos trigger")
        servoang = servoang + 1
        time.sleep(.01)
    my_servo.angle = servoang
    print(servoang)
    if servoang > 179:
        print("POS max")
        servoang = 178
        time.sleep(.5)
    if servoang < 1:
        print("NEG max")
        servoang = 2
        time.sleep(.5)