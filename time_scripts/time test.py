import datetime
import time

old_clock = datetime.datetime.now()

def clock_text(time):
    if time.hour < 10:
        hour = "0" + str(time.hour)
    if time.minute < 10:
        minute = "0" + str(time.minute)
    return hour + ":" + minute

print(clock_text(old_clock))
while True:
    clock = datetime.datetime.now()
    if clock.minute != old_clock.minute:
        print(clock_text(clock))
    old_clock = datetime.datetime.now()
    # time.sleep() reduserer prosessorbruken enormt utan å påvirke funksjonaliteten
    time.sleep(0.05)
