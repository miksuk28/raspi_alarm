class Day:
    def __init__(self, day, alarm_hour, alarm_minute, offset_minute):
        self.day = day
        self.alarm_hour = alarm_hour
        self.alarm_minute = alarm_minute

        def sub_time(self, offset_minute):
            new_hour = self.alarm_hour
            new_minute = self.alarm_minute
            if (self.alarm_minute - offset_minute) < 0:
                new_hour = new_hour - (offset_minute // 60)
                new_minute = new_minute - self.alarm_minute - (offset_minute // 60)

            return new_hour, new_minute

        self.offset = sub_time(self, offset_minute)


monday = Day("monday", 6, 30, 40)
print("The alarm on " + monday.day + " is at " + str(monday.alarm_hour) + ":" + str(monday.alarm_minute) + " O' clock.")

print(monday.offset)
