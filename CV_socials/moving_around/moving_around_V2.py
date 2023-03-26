import math
import pyautogui
import time
import random

while True:
    time.sleep(3)
    # Define the screen size
    SCREEN_WIDTH, SCREEN_HEIGHT = pyautogui.size()

    # Define the location coordinates
    LOCATION_X = int(SCREEN_WIDTH * 0.5)  # Move to the center of the screen horizontally
    LOCATION_Y = int(SCREEN_HEIGHT * 0.5)  # Move to the center of the screen vertically

    # Move the cursor to a random location on the screen with random offset
    print("Move the cursor to a random location on the screen with random offset")
    random_x = random.randint(0, SCREEN_WIDTH)
    random_y = random.randint(0, SCREEN_HEIGHT)
    pyautogui.moveTo(random_x + random.randint(-50, 50), random_y + random.randint(-50, 50))

    # Move the cursor in a circle for 5 seconds
    # while time.time() - start_time < 5:

    print("circling")
    start_time = time.time()
    for i in range(7):
        x_offset = int(50 * math.cos((time.time() - start_time) * math.pi))
        y_offset = int(50 * math.sin((time.time() - start_time) * math.pi))
        pyautogui.moveRel(x_offset, y_offset)
        time.sleep(0.05)

    print("pause")
    # Wait for a random amount of time before moving again
    pyautogui.PAUSE = random.uniform(15, 55)

    # Move slightly around the location coordinates with random offset
    print("move rel last")
    pyautogui.moveRel(random.randint(-50, 50), random.randint(-50, 50))

    #time.sleep(random.uniform(1000, 2500))
    time.sleep(random.uniform(1, 2))