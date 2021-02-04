import pigpio
import time
import random
from subprocess import call

call(["sudo", "pigpiod"])
pi = pigpio.pi()

R = 17
G = 22
B = 24

while True:
    pi.set_PWM_dutycycle(R, random.randint(100, 255)
    pi.set_PWM_dutycycle(G, random.randint(100, 255)
    pi.set_PWM_dutycycle(B, random.randint(100, 255)

    time.sleep(0.05)
