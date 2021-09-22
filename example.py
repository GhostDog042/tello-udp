import time
from tello import Tello

# Make a connection object
myTello = Tello()

# enable network commands on the drone
myTello.send("command")

# takeoff
myTello.send("takeoff")

start = time.time()

# wait 30 seconds
while time.time() - start < 30:
    # query battery info to prevent tello connection from timing-out
    myTello.send("battery?")
    time.sleep(1)

# land the tello
myTello.send("land")

