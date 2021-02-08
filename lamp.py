import time
import datetime
import configparser

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
date = datetime.datetime.today()
config = configparser.ConfigParser
config.read("config.ini")

class Today:
    def __init__(self, alarm_state, alarm_hour, alarm_minute):
        self.day = weekdays[date.weekday()]
        self.alarm_state = config[self.day]["alarm_state"]
        self.alarm_hour = config[self.day]["alarm_hour"]
        self.alarm_minute = config[self.day]["alarm_minute"]

running = True

def main():
    config.read("config.ini")
    while running:
        pass

main()
