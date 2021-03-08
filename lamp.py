# debug modus for testing
debug = False

from time import *              # sleep() for å kunne vente
from datetime import *          # handtering av dagar og klokkeslett
from threading import Thread    # threading, for å kunne ha ein timar som køyrer parallellt i bakgrunnen
import configparser             # for å lese config filer der alarmane og innstillingane er lagra

# importerer ikkje Raspi moduler dersom debug == True
if not debug:
    import pigpio
    from subprocess import call

    # caller pigpiod gjennom terminalen
    call("sudo pigpiod", shell=True)
    pi = pigpio.pi()

# pinnummer for lys og brytar
R = 17
G = 22
B = 24
BTN = 27

weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

# laster inn og les konfigurasjonsfila
config = configparser.ConfigParser()
config.read("config.ini")

# sjekker om knapp er på når kalla: returnerer bool (om pin 27 ikkje les 0)
def check_button():
    if pi.read(BTN) != 0:
        return True
    else:
        return False

# simpelt klokkeobjekt: ikkje så veldig nyttig, bør kanskje fjernast
class Clock:
    def __init__(self):
        self.h = int(datetime.now().strftime("%H"))
        self.m = int(datetime.now().strftime("%M"))
        print(self.h, self.m)

clock = Clock()

# timer som køyrer i anna thread uavhengig av hovudprogrammet
def timer():
    global time_mins
    while True:
        hour = int(datetime.now().strftime("%H"))
        minutes = int(datetime.now().strftime("%M"))
        time_mins = (hour * 60) + minutes
        print(time_mins)
        sleep(1)

# deklarerer og starter threaden
timer_thread = Thread(target = timer)
timer_thread.start()

# omrekner og returnerer timar og minutt til tal minutt
def calc_mins(hours, minutes):
    return (hours * 60) + minutes

# oppdaterer alarmen: les frå konfig-fila på nytt og lagrar framtidige alarmar i ei liste
def update_alarm():
    config.read("config.ini")

    # sletter alt innholder i listene
    global alarms
    global settings
    alarms = []
    settings = []
    day = datetime.now().weekday()
    
    # setter preferansane
    settings = [
        {"lamp_mode" : {"red" : int(config["LAMP_MODE"]["RED"]), "green" : int(config["LAMP_MODE"]["GREEN"]), "blue" : int(config["LAMP_MODE"]["BLUE"])}},
        {"pref" : {"red" : int(config["PREF"]["RED"]), "green" : int(config["PREF"]["GREEN"]), "blue" : int(config["PREF"]["BLUE"]), "offset" : int(config["PREF"]["offset"])}}
    ]
    # alarms = [{"day" : "Monday", "alarm_state" : True, "alarm_hour" : 6, "alarm_minute" : 10}]
    
    # sjekker berre tom. sondag. Legg til unntak for sondag-mandag
    # cycler gjennom og legger til framtidige alarmer til lista, sjekker i config fila
    for i in range(day, 7):
        if config[weekdays[i]]["alarm_state"] == "1":
            mins = calc_mins(int(config[weekdays[i]]["alarm_hour"]), int(config[weekdays[i]]["alarm_minute"]))
            alarm_day = {"day" : weekdays[i], "alarm_state" : True, "alarm_hour" : int(config[weekdays[i]]["alarm_hour"]), "alarm_minute" : int(config[weekdays[i]]["alarm_minute"]), "mins" : mins, "mins_offset" : mins - settings[1]["pref"]["offset"]}
            alarms.append(alarm_day)

# setter led verdi og lagrer noverande verdi i globale variablar
def led_set(r, g, b):
    global red, green, blue
    red = r
    blue = b
    green = g

    pi.set_PWM_dutycycle(R, r)
    pi.set_PWM_dutycycle(G, g)
    pi.set_PWM_dutycycle(B, b)

    if debug: print(r, g, b)

# slår av leds
def led_off():
    led_set(0,0,0)

# linær interpolasjon for fading mellom to verdiar, funkar sikkert ikkje enda
def interpolate(r1, g1, b1, r2, g2, b2, steps, pause):
    r_ = (r2 - r1) / steps
    g_ = (g2 - g1) / steps
    b_ = (b2 - b1) / steps

    for i in range(steps):
        led_set((r1 - (r_ * i)), (g1 - (g_ * i)), (b1 - (b_ * i)))

# fades off
def fade_off():
    pass

# potensiell boot-animasjon
def boot_animation():
    led_off()
    p = 0.005 # pause
    for i in range(2):
        for i in range(255):
            led_set(0, i, 0)
            sleep(p)
        for i in range(255, 0, -1):
            led_set(0, i, 0)
            sleep(p)

update_alarm()
print(settings)
print(alarms)

# boot_animation()
print("gaming")

print(settings[0]["lamp_mode"]["red"], settings[0]["lamp_mode"]["green"], settings[0]["lamp_mode"]["blue"])

# main loop der alt skjer, bør kanskje vere i ein funksjon
while True:
    led_set(settings[0]["lamp_mode"]["red"], settings[0]["lamp_mode"]["green"], settings[0]["lamp_mode"]["blue"])
    if check_button():
        print("gaming")
