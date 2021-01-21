import time
vals = []

def led_off():
    #this should turn off the LED strip
    print("LED strip is off")

def led_set(r, g, b):
    #sets LED strip to RGB values
    print("Led set to (" + str(r) + ", " + str(g) + ", "+ str(b) + ")")

def interpolate(r1, g1, b1, r2, g2, b2, steps, cycle):
    r = (r2 - r1) / steps*cycle
    g = (g2 - g1) / steps*cycle
    b = (b2 - b1) / steps*cycle

    return int(r), int(g), int(b)

def sub_time(hour_start, minute_start, hour_sub, minute_sub):
    if (hour_start - hour_sub) < 0:
        new_hour = (hour_start - hour_sub) *-1
    else:
        new_hour = hour_start - hour_sub
    if (minute_start - minute_sub) < 0:
        new_minute = (minute_start - minute_sub) *-1
        new_hour -= 1
    else:
        new_minute = minute_start - minute_sub

    return new_hour, new_minute

def sub_time(hour_start, minute_start, hour_sub, minute_sub):
    if (hour_start - hour_sub) < 0:
            new_hour = (hour_start - hour_sub) *-1
    else:
        new_hour = hour_start - hour_sub


def time_dif(h1, m1, h2, m2):
    if(h1 == h2):
        return m2-m1
    else:
        return ((h2-h1-1)*60 + (60-m1) + m2)

if False:
    for i in range(1800):
        current_val = interpolate(0, 0, 0, 255, 255, 255, 1800, i)
        if not vals:
            vals.append((0, 0, 0))
        if current_val != vals[-1]:
            vals.append(current_val)

print(vals)

print(time_dif(12, 30, 2, 20))