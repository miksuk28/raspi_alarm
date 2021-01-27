import datetime
import time

# min and max values for time
min = 0
max = 1440
time = datetime.datetime.now()
print(time)

def sub_time(h, m, min_offset):
    """Tar start-, sluttid og minutt å trekke frå og returnerer klokkeslettet"""
    mins = ((h*60) + m) - min_offset
    if mins < 0:
        mins = mins * -1
    if mins > max:
        mins -= ((mins // max)*max)

    return mins_to_time(mins)

def mins_to_time(mins):
    """konverterer frå minutt til timer og minutt"""
    h = mins // 60
    m = mins - ((mins // 60)*60)

    return h, m

def print_time(h, m):
    """printer tida i leseleg format: tt:mm"""
    time_str = ""
    if h < 10:
        time_str = "0" + str(h)
    else:
        time_str += str(h)
    time_str += ":"
    if m < 10:
        time_str += "0" + str(m)
    else:
        time_str += str(m)

    print(time_str)

# trekker frå 1000 min frå 06:00
print(sub_time(6, 0, 1000))

