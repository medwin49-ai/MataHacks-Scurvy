from datetime import datetime
import time

terminateLoop = False
# The clock function is a timer that goes down depending on the users input (Input is measerused in seconds)(for now).
def theClock(UserTime):
    defaultinteral: int = 60

    if UserTime != 0:
        while UserTime >= 0:
            m, s = divmod(UserTime, 60)
            h, m = divmod(m, 60)
            time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
            print(time_left + "\r", end=time_left)
            time.sleep(1)
            UserTime -= 1

    else:
        theClock(defaultinteral)

    return


# This function shows the User the live feed of time.
def LiveLocalTime():
    global terminateLoop
    while terminateLoop == False:
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        print("\r" + current_time + " Press enter to exit" , end = "")
        time.sleep(1)


# This function shows the user the time it was used.
def currentLocalTime():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    print(current_time + "\r", end=current_time)
    return
