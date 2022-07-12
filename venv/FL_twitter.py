import pyautogui as p
import time

#view1Location = [785, 496]
#subscribeLocation = [903, 330]
#closeWindowLocation = [981, 14]
#resfreshLocation = [78, 58]

view1Location = [549, 497]
followLocation = [736, 340]
closeWindowLocation = [984, 9]
confirmLocation =  [816, 567]
resfreshLocation = [55.49375, 41.24444444444445]

retweetLocation = [517, 395]
closeWindowLocation2 = [983, 18]

def twitter_flw():
    while True:
        time.sleep(3)
        p.click(view1Location)
        time.sleep(6)
        p.click(followLocation)
        time.sleep(4)
        p.click(closeWindowLocation)
        time.sleep(4)
        p.click(confirmLocation)
        time.sleep(8)
        p.click(resfreshLocation)
        time.sleep(3)

def twitter_retweet():
    while True:
        time.sleep(3)
        p.click(view1Location)
        time.sleep(6)
        p.click(retweetLocation)
        time.sleep(4)
        p.click(closeWindowLocation2)
        time.sleep(4)
        p.click(confirmLocation)
        time.sleep(8)
        p.click(resfreshLocation)
        time.sleep(3)
twitter_retweet()
#twitter_flw()