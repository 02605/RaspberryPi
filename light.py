import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.OUT)

try:
    t = 0.05
    while True:
        GPIO.output(40, True)
        time.sleep(t)
        GPIO.output(40, False)
        time.sleep(t)

except KeyboardInterrupt:
    pass

print("over....")
GPIO.cleanup()

