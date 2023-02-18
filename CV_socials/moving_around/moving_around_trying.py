import pyautogui
import random

# Define the screen resolution variables
SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

while True:
    # Define the location coordinates
    LOCATION_X = int(SCREEN_WIDTH * 0.5) # Move to the center of the screen horizontally
    LOCATION_Y = int(SCREEN_HEIGHT * 0.5) # Move to the center of the screen vertically

    # Move the cursor to the location coordinates with random offset
    pyautogui.moveTo(LOCATION_X + random.randint(-50, 50), LOCATION_Y + random.randint(-50, 50))

    # Wait for a random amount of time before moving again
    pyautogui.PAUSE = random.uniform(0.5, 2.0)

    # Move slightly around the location coordinates with random offset
    pyautogui.moveRel(random.randint(-50, 50), random.randint(-50, 50))
