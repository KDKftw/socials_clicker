import pyautogui as p
import time

#view1Location = [785, 496]
#subscribeLocation = [903, 330]
#closeWindowLocation = [981, 14]
#resfreshLocation = [78, 58]

view1Location = [558.4947916666667, 352.7111111111111]
subscribeLocation = [642.446875, 234.66666666666669]
closeWindowLocation = [697.9406250000001, 9.955555555555556]
resfreshLocation = [55.49375, 41.24444444444445]

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