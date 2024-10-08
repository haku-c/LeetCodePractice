# Part 1:
# Write a logger that logs an event by its string ID and its duration. You start logging an event by calling .startLog(String id) and end the event by calling .endLog(String id). For example:

# Logger myLogger(...);
# myLogger.startLog("A");
# myLogger.startLog("B");
# myLogger.endLog("A");
# myLogger.endLog("B");

# When you call end log, the logger will print the ID and the duration of that event to the console.

# myLogger.endLog("A");
# A, 3 seconds

# myLogger.endLog("B");
# B, 4 seconds

# _____________________________

# Part 2:
# Now, we want the logger to only print the events in chronological order based on the start log time. The logger will print an ID and duration if and only if all events that were started before this ID have already ended.

# The logger should print ALL events that have ended that meet the above constraint.

# For example, if we call:

# myLogger.startLog("A");
# myLogger.startLog("B");
# myLogger.endLog("B");

# Nothing would print because although B has ended, A has not ended yet and it was started before B.

# Once we call:
# myLogger.endLog("A");

# then it will print BOTH A and B:
# A, 5 seconds
# B, 2 seconds

import time


class Logger:
    def __init__(self):
        self.log = []
        self.printed = {}

    def startLog(self, id):
        self.log.append((id, time.time(), -1))
        self.printed[id] = False

    def endLog(self, id):
        for i in range(len(self.log)):
            currentId, currentTime, _ = self.log[i]
            if currentId == id:
                self.log[i] = (id, currentTime, time.time() - currentTime)

        for i in range(len(self.log)):
            currentId, currentTime, currentDuration = self.log[i]
            if currentDuration == -1:
                break
            elif not self.printed[currentId]:
                print(currentId + ", " + str(currentDuration))
                self.printed[currentId] = True


myLogger = Logger()
myLogger.startLog("A")
time.sleep(3)
myLogger.endLog("A")
