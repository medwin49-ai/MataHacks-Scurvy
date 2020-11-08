from datetime import datetime
import time

#The clock function is a timer that goes down depending on the users input (Input is measerused in seconds)(for now).
def theClock():
    while True:
        uin = input(">> ")
        try:
            when_to_stop: int = abs(int(uin))
        except KeyboardInterrupt:
            break

        while when_to_stop >= 0:
            m, s = divmod(when_to_stop, 60)
            h, m = divmod(m, 60)
            time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
            print(time_left + "\r", end=time_left)
            time.sleep(1)
            when_to_stop -= 1

        return

#This function shows the User the live feed of time.
def LiveLocalTime():
    while True:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print(current_time + "\r", end=current_time)
        time.sleep(1)

#This function shows the user the time it was used.
def currentLocalTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time + "\r", end=current_time)
    return