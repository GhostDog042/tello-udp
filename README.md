# tello-udp
Dead-simple code for connecting to the Ryze Tello with udp and python
Originally made by alecGraves, remixed by GhostDog042

## Manual Usage
* Connect to the tello's wi-fi network
* ```python tello.py ```
* Just type a command (see below) and press enter to send it.

## Example Program
```python
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

```

## Message Guide
* ```connect``` = enable commands, also resets emergency mode
* ```takeoff``` = take off, hovering at approximately 1 meter
* ```land``` = gradually land
* ```emergency``` = immediately stop all motors, causing the drone to fall out of the sky
* ```forward x``` = go forward ```x``` centi-meters (cm)
* ```back x``` = go back ```x``` cm
* ```left x``` = go left ```x``` cm
* ```right x``` = go right ```x``` cm
* ```ccw x``` = rotate counter-clockwise ```x``` degrees
* ```cw x``` = rotate clockwise ```x``` degrees
* ```flip f/b/l/r``` = flip forward/back/left/right
* ```battery?``` = return current battery ("100" for 100%)
* Full SDK command list is available at the [Ryze Tello Downloads Page](https://www.ryzerobotics.com/tello/downloads)


## Known Issues
* The Tello connection will time out in 15 seconds of no messages, causing the drone to land.
This should be resolved by threading to periodically send messages.


## All Commands
Command | Description | Response

command | Enter command mode | OK|False

end | Exits the loop in tello.py, only appilcable there though | N/A

takeoff | Auto takeoff | OK|False

land | Auto landing | OK|False

up xx | Fly upward [20, 500] cm | OK|False

down xx | Fly downward [20, 500] cm | OK|False

left xx | Fly left [20, 500] cm | OK|False

right xx | Fly right [20, 500] cm | OK|False

forward xx | Fly forward [20, 500] cm | OK|False

cw xx | Rotate clockwise [1, 360] degrees | OK|False

ccw xx | Rotate counter-clockwise [1, 360] | degrees OK|False

flip x | Flip [l, r, f, b] | OK|False

speed xx | Set speed [1, 100] cm/s | OK|False

Speed? | Get current speed | xx

Battery? | Get current battery percentage | xx

Time? | Get current flight time | xx
