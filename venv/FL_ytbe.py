import pyautogui as p
import time

view1Location = [785, 496]
subscribeLocation = [903, 330]
closeWindowLocation = [981, 14]

time.sleep(3)
p.click(view1Location)
time.sleep(6)
p.click(subscribeLocation)
time.sleep(3)
p.click(closeWindowLocation)