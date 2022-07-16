import cv2
import numpy as np


import time
import pyautogui

time.sleep(5)
##take screen on initial page, save, find view, get location, click
myScreenshot = pyautogui.screenshot()
myScreenshot.save('findView.png')
screenshot = cv2.imread("findView.png", 0)
template = cv2.imread("view2.png",  0)
res = cv2.matchTemplate(screenshot, template, cv2.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
viewLocator = min_loc
time.sleep(2)
pyautogui.click(viewLocator)






#template = cv2.imread("thumbsUP.png",  0)
print(min_loc)      ##(648, 870)