import pyautogui as p
import time

view1Location = [539, 474]
followLocation = [348, 251]
closeWindowLocation = [984, 20]
confirmLocation =  [824, 545]
resfreshLocation = [55.49375, 41.24444444444445]

def tik_flw():
    while True:
        time.sleep(3)
        p.click(view1Location)
        time.sleep(6)
        p.click(followLocation)
        time.sleep(10)
        p.click(closeWindowLocation)
        time.sleep(8)
        p.click(confirmLocation)
        time.sleep(6)
        p.click(resfreshLocation)
        time.sleep(3)
tik_flw()