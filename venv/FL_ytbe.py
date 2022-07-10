import pyautogui as p
import time

view1Location = [785, 496]
subscribeLocation = [903, 330]
closeWindowLocation = [981, 14]
resfreshLocation = [78, 58]



while True:
    time.sleep(3)
    p.click(view1Location)
    time.sleep(6)
    p.click(subscribeLocation)
    time.sleep(4)
    p.click(closeWindowLocation)
    time.sleep(12)
    p.click(resfreshLocation)
    time.sleep(3)