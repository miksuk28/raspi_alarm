from time import *
from datetime import *
import threading
import configparser

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

config = configparser.ConfigParser()
config.read("config.ini")
running = True

# testing
def check_button():
    return True

class Clock:
    def __init__(self):
        self.h = int(datetime.now().strftime("%H"))
        self.m = int(datetime.now().strftime("%M"))
        print(self.h, self.m)

clock = Clock()

# køyr i anna thread
def timer():
    global timer
    while True:
        timer = 0
        for x in range(60):
            # print(timer)
            timer += 1
            clock.__init__()
            sleep(1)

timer_thread = threading.Thread(target = timer)
timer_thread.start()

class NextAlarm:
    def __init__(self):
        day = weekdays[datetime.now().weekday()]
        if int(config[day]["alarm_state"]):
            pass

        self.day = weekdays[datetime.now().weekday()]
        self.alarm_state  = str(config[self.day]["alarm_state"])
        self.alarm_hour   = str(config[self.day]["alarm_hour"])
        self.alarm_minute = str(config[self.day]["alarm_minute"])

alarm = NextAlarm()

def main():
    config.read("config.ini")
    if check_button():
        pass

main()
