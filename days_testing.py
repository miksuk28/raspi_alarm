class Day:
    def __init__(self, day, alarm_hour, alarm_minute, offset_minute):
        self.day = day
        self.alarm_hour = alarm_hour
        self.alarm_minute = alarm_minute
        self.offset = self.sub_time(self, offset_minute)

    def sub_time(self, offset_minute):
        new_hour = self.alarm_hour
        if (self.alarm_minute - self.offset) < 0:
            new_hour -= (self.offset // 60)


monday = Day("monday", 6, 30, 30)
print("The alarm on " + monday.day + " is at " + str(monday.alarm_hour) + ":" + str(monday.alarm_minute) + " O' clock.")
