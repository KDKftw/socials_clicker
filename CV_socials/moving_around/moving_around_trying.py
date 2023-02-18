import pyautogui
import random
import time



# Define the screen resolution variables
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

while True:
    time.sleep(3)
    # Define the location coordinates
    LOCATION_X = int(SCREEN_WIDTH * 0.5) # Move to the center of the screen horizontally
    LOCATION_Y = int(SCREEN_HEIGHT * 0.5) # Move to the center of the screen vertically

    # Move the cursor to the location coordinates with random offset
    pyautogui.moveTo(LOCATION_X + random.randint(-50, 50), LOCATION_Y + random.randint(-50, 50))

    # Wait for a random amount of time before moving again
    pyautogui.PAUSE = random.uniform(15, 55)
    print("pyautogui.PAUSE = random.uniform(15, 55)")

    # Move slightly around the location coordinates with random offset
    pyautogui.moveRel(random.randint(-50, 50), random.randint(-50, 50))
    print("pyautogui.moveRel(random.randint(-50, 50), random.randint(-50, 50))")


    time.sleep(random.uniform(1000, 2500))
    #time.sleep(random.uniform(1, 2))