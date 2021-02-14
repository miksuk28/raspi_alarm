from time import *
from datetime import *
import threading
import configparser
import pigpio

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
    return pi.read(BTN)

def calcmins(hours, mins):
    '''calculates hours and minutes to total minutes'''
    return (hours * 60) + mins

# koyr i anna thread
def timer():
    global mins
    while True:
        hr = int(datetime.now().strftime("%H"))
        min = int(datetime.now().strftime("%M"))
        mins = calcmins(hr, min)
        print(mins)
        sleep(1)

timer_thread = threading.Thread(target = timer)
timer_thread.start()

class NextAlarm:
    def __init__(self):
        day = weekdays[datetime.now().weekday()]
        day_num = datetime.now().weekday()

        while True:
            if day_num > 6:
                break
            if int(config[weekdays[day_num]]["alarm_state"]):
                self.day = weekdays[day_num]
                break
            else:
                day_num += 1


        self.offset = int(config["PREF"]["offset"])
        self.alarm_state = bool(config[self.day]["alarm_state"])
        self.alarm = calcmins(config[self.day]["alarm_hour"], config[self.day]["alarm_minute"])
        self.alarm_start = self.alarm - self.offset

alarm = NextAlarm()

def main():
    config.read("config.ini")
    if check_button():
        pass

# will reload if broken out of loop
main()
