import pyautogui
"""
----------------------------------------------------------------------------------
>>>>>>>>>>>>>>>>>>>>> CONSTANTS need to be updated by user   <<<<<<<<<<<<<<<<<<<<<
----------------------------------------------------------------------------------
"""
#Constants
MINUTES = 1 #user input minutes for timer countdown
INTERVAL = 10 #user input for interval in seconds to be notified and for the loop to perform


  
def main():
      #variables
    timer = int(MINUTES * 60 / INTERVAL)
    clicks = 0
    time_left = (MINUTES * 60) - (clicks * INTERVAL)
    print(f"You have {time_left} seconds remaining.")

    for i in range(timer):
        pyautogui.sleep(INTERVAL) # same for ALL
        pyautogui.click((1274, 545), duration =0.1) #only for the 1st time
        clicks += 1
        time_left = (MINUTES * 60) - (clicks * INTERVAL)
        print(f"You have {time_left} seconds remaining.")  #in seconds

if __name__ == "__main__":
    main()