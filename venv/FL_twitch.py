view1Location = [539, 474]
import pyautogui as p
import time

view1Location = [539, 472]
followLocation = [1183, 627]
followLocation2 = [982, 633]
closeWindowLocation = [1349, 17]
confirmLocation =  [824, 546]
resfreshLocation = [55.49375, 41.24444444444445]
maximizeLocation = [933, 10]


def twitch_flw():
    while True:
        time.sleep(3)
        p.click(view1Location)
        time.sleep(1)
        p.click(maximizeLocation)
        time.sleep(13)
        p.click(followLocation2)
        time.sleep(2)
        p.click(followLocation)
        time.sleep(6)
        p.click(closeWindowLocation)
        time.sleep(4)
        p.click(confirmLocation)
        time.sleep(6)
        p.click(resfreshLocation)
        time.sleep(3)
twitch_flw()