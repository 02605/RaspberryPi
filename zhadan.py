import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

try:
    t = 0.05
    while True:
        GPIO.output(11, True)
        time.sleep(t)
        GPIO.output(11, False)
        time.sleep(t)

except KeyboardInterrupt:
    pass

print("over....")
GPIO.cleanup()

