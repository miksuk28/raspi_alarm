from time import *
from datetime import *
from threading import Thread
import configparser

alarms = []
settings = []
weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

debug = True

if not debug:
    call("sudo pigpiod", shell=True)
    pi = pigpio.pi()

R = 17
G = 22
B = 24
BTN = 27

config = configparser.ConfigParser()
config.read("config.ini")

day = datetime.now().weekday()
hour = int(datetime.now().strftime("%H"))
minute = int(datetime.now().strftime("%M"))

print("Today is " + weekdays[day] + " and the time is " + str(hour) + ":" + str(minute))

def calc_mins(hours, minutes):
    return (hours * 60) + minutes

class Alarm:
    def __init__(self, day, hour, minute):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.mins = calc_mins(hour, minute)

'''
def update_alarm():
    day = datetime.now().weekday()
    if bool(config[weekdays[day]]["alarm_state"]):
        weekday = weekdays[day]
        alarm = Alarm(weekday, int(config[weekday]["alarm_hour"]), int(config[weekday["alarm_minute"]]))
    else:
'''

def update_alarm():
    # sletter alt innholder i lista
    global alarms
    global settings
    alarms = []
    day = datetime.now().weekday()

    settings = [
        {"lamp_mode" : {"red" : int(config["LAMP_MODE"]["RED"]), "green" : int(config["LAMP_MODE"]["GREEN"]), "blue" : int(config["LAMP_MODE"]["BLUE"])}},
        {"pref" : {"red" : int(config["PREF"]["RED"]), "green" : int(config["PREF"]["GREEN"]), "blue" : int(config["PREF"]["BLUE"])}}
    ]

update_alarm()
print(settings)