from datetime import *
import time
import threading

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

def calcmins(hours, minutes):
    return hours*minutes

# virker med antal minutt per døgn
def timer():
    global time_mins
    while True:
        hour = int(datetime.now().strftime("%H"))
        minutes = int(datetime.now().strftime("%M"))
        time_mins = (hour * 60) + minutes
        print(time_mins)
        time.sleep(1)

timermins_thread = threading.Thread(target = timer)
timermins_thread.start()
