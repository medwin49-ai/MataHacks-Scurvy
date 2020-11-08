from datetime import datetime
import time

now = datetime.now()
current_time = now.strftime("%H:%M")

targetTime = 0
Zone = 0
defaultInterval = 10

print("Input how many seconds")
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
        print(time_left + "\r",   end=time_left)
        time.sleep(1)
        when_to_stop -= 1

    print("\nPlease Mediate :)")