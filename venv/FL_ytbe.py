import pyautogui as p
import time

#view1Location = [785, 496]
#subscribeLocation = [903, 330]
#closeWindowLocation = [981, 14]
#resfreshLocation = [78, 58]

view1Location = [549, 497]
subscribeLocation = [906, 332]
closeWindowLocation = [995, 24]
resfreshLocation = [55.49375, 41.24444444444445]
def ytbe_sub():
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
#likeLocation = [65, 620]
likeLocation = [65, 633]
view1Location2 = [541, 473]

def ytbe_like():
    while True:
        time.sleep(3)
        p.click(view1Location2)
        time.sleep(10)
        p.click(likeLocation)
        time.sleep(6)
        p.click(closeWindowLocation)
        time.sleep(12)
        p.click(resfreshLocation)
        time.sleep(3)

#ytbe_like()
ytbe_sub()