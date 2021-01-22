import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

RED = 17
GREEN = 22
BLUE = 24

GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

def off():
    GPIO.output(RED, 0)
    GPIO.output(GREEN, 0)
    GPIO.output(BLUE, 0)
    
def led_write(r, g, b):
    GPIO.PWM(RED, r)
    GPIO.PWM(GREEN, g)
    GPIO.PWM(BLUE, b)

time.sleep(1)

off()
GPIO.output(RED, 255)
GPIO.output(GREEN, 255)
GPIO.output(BLUE, 255)
time.sleep(1)

GPIO.output(RED, 100)
GPIO.output(GREEN, 50)
GPIO.output(BLUE, 0)
time.sleep(1)

print("Attempting fade")
off()
for i in range(255):
    i += 1
    print(i)
    led_write(i, i, i)
    time.sleep(0.5)
    
GPIO.cleanup()
