import oClock
import threading

def clocthreadfunc():
    oClock.LiveLocalTime()
backgroundThread = threading.Thread(group = None, target = clocthreadfunc , name="clockthread" , daemon= True )


oClock.currentLocalTime()
print("\n" + "Input how many seconds")
userInput = input(">> ")
oClock.theClock(abs(int(userInput)))
print("\nPlease Mediate :)")
backgroundThread.start()
while True:
    userchoice = input()
    oClock.terminateLoop = True
    break
backgroundThread.join()

print("Thread has exit")