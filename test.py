import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

RED = 17
GREEN = 22
BLUE = 24

GPIO.setup(RED, GPIO.OUT)
GPIO.output(RED, 128)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.output(GREEN, 128)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.output(BLUE, 128)
