import pigpio
from subprocess import call
from time import *
from datetime import *
import threading
import configparser

call("sudo pigpiod", shell=True)
pi = pigpio.pi()

R = 17
G = 22
B = 24
BTN = 27

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

config = configparser.ConfigParser()
config.read("config.ini")
running = True

# testing
def check_button():
    if pi.read(BTN) != 0:
        return True
    else:
        return False

class Clock:
    def __init__(self):
        self.h = int(datetime.now().strftime("%H"))
        self.m = int(datetime.now().strftime("%M"))
        print(self.h, self.m)

clock = Clock()

# køyr i anna thread
def timer():
    global time_mins
    while True:
        hour = int(datetime.now().strftime("%H"))
        minutes = int(datetime.now().strftime("%M"))
        time_mins = (hour * 60) + minutes
        print(time_mins)
        sleep(1)

timer_thread = threading.Thread(target = timer)
timer_thread.start()

def get_alarm_mins(day):
    day_name = weekdays[day]

    minutes = int(config[day_name]["alarm_minute"])
    hours = int(config[day_name]["alarm_hour"])

    return (hours * 60) + minutes

class NextAlarm:
    def __init__(self):
        day = datetime.now().weekday()
        count = 0
        while True:
            if count > 6:
                break
            elif bool(config[weekdays[day]]["alarm_state"]) and get_alarm_mins(day) > time_mins:
                self.day = weekdays[day]
                self.day_num = day
                break
            else:
                day += 1
                count += 1

        self.alarm_state  = str(config[self.day]["alarm_state"])
        self.alarm_hour   = str(config[self.day]["alarm_hour"])
        self.alarm_minute = str(config[self.day]["alarm_minute"])

alarm = NextAlarm()

def led_set(r, g, b):
    global red, green, blue
    red = r, blue = b, green = g

    pi.set_PWM_dutycycle(R, r)
    pi.set_PWM_dutycycle(G, g)
    pi.set_PWM_dutycycle(B, b)

    if debug: print(r, g, b)

def led_off():
    led_set(0,0,0)

def interpolate(r1, g1, b1, r2, g2, b2, steps, pause):
    r_ = (r2 - r1) / steps
    g_ = (g2 - g1) / steps
    b_ = (b2 - b1) / steps

    for i in range(steps):
        led_set((r1 - (r_ * i)), (g1 - (g_ * i)), (b1 - (b_ * i)))

# fades off
def fade_off():
    pass

def main():
    config.read("config.ini")
    if check_button():
        led_off()
        if alarm.alarm_state:
            pass

# will reload if broken out of loop
main()
