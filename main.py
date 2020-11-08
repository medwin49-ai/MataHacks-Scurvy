import oClock
import threading


def clocthreadfunc():
    oClock.LiveLocalTime()


backgroundThread = threading.Thread(group=None, target=clocthreadfunc, name="clockthread" )



oClock.currentLocalTime()
print("\n" + "Input how many seconds")
userInput = input(">> ")
oClock.theClock(abs(int(userInput)))
print("\nPlease Meditation :)")
backgroundThread.start()
while True:
    userchoice = input()
    oClock.terminateLoop = True
    break

backgroundThread.join()
print("You have exited Meditation")


print("Goodbye :)")
