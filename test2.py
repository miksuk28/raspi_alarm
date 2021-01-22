import pigpio
import time
from subprocess import call

call("sudo pigpiod", shell=True)
pi = pigpio.pi()

RED = 17
GREEN = 22
BLUE = 24

def led_off():
    led_set(0,0,0)
    print("Strip slatt av")

def led_set(r, g, b):
    pi.set_PWM_dutycycle(RED, r)
    pi.set_PWM_dutycycle(GREEN, g)
    pi.set_PWM_dutycycle(BLUE, b)
    print("Satt LED verdi: (" + str(r) + ", " + str(g) + ", " + str(b) + ")")

led_off()
for i in range(255):
    led_set(i, i, i)
    print(i)
    time.sleep(0.1)
