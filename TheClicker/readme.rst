Welcome to trick the boss clicker
*********************************

Instructions to use
-------------------

The CONSTANTS below require a user input.

MINUTES: for how long the loop will execute (unit: minutes).
INTERVAL: frequency of the notification of how many seconds left in the timer (unit: seconds).

MINUTES = 1
INTERVAL = 10

This script uses the pyautogui module. To install, execute the below line in your compiler terminal:

pip install -r requirements.txt

NOTE: this program positions the mouse cursor in the center of the screen and automatically clicks as per the user inputs in the minutes and interval constants. The user needs to ensure that there is nothing in the center of the screen that, if clicked on, can produce undesirable results.

Since we have a mouse replicator loop, there is a failsafe to stop and exit the program: move the cursor to the top left corner of the screen (coordinates x=0, y=0).