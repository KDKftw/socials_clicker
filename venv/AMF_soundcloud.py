import pyautogui as p
import time


def SC_LikeClose():
    time.sleep(16)
    p.click(47, 574)
    time.sleep(7)
    p.click(691, 8)
    time.sleep(10)

def tiktokClickThrough_REFRESHED2():
    time.sleep(4)
    p.click(684, 419)
    SC_LikeClose()

def SC_like():
    tiktokClickThrough_REFRESHED2()
    resetCounter = 0
    while True:
        time.sleep(4)
        p.click(691, 488)
        SC_LikeClose()
        resetCounter = resetCounter + 1
        print(resetCounter)
        time.sleep(6)

        if resetCounter == 2:
            p.click(93, 61)
            time.sleep(3)
            tiktokClickThrough_REFRESHED2()
            resetCounter = 0
        else:
            pass

SC_like()