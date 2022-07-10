import pyautogui as p
import time

def tiktokFollowClose():
    time.sleep(13)
    p.click(350, 254)
    time.sleep(7)
    p.click(683, 16)
    time.sleep(13)

def tiktokClickThrough_REFRESHED():
    time.sleep(4)
    p.click(683, 405)  ##first one flw
    tiktokFollowClose()

def tiktokLikeClose():
    time.sleep(13)
    p.click(621, 586)
    time.sleep(7)
    p.click(677, 18)
    time.sleep(13)

def tiktokClickThrough_REFRESHED2():
    time.sleep(4)
    p.click(683, 405)
    tiktokLikeClose()


def tiktok():
    tiktokClickThrough_REFRESHED()
    resetCounter = 0
    while True:
        time.sleep(4)
        p.click(684, 489)
        tiktokFollowClose()
        resetCounter = resetCounter + 1
        print(resetCounter)
        time.sleep(6)

        if resetCounter == 2:
            p.click(93, 61)
            time.sleep(3)
            tiktokClickThrough_REFRESHED()
            resetCounter = 0
        else:
            pass
def tiktok_liking():
    tiktokClickThrough_REFRESHED2()
    resetCounter = 0
    while True:
        time.sleep(4)
        p.click(684, 489)
        time.sleep(3)
        tiktokLikeClose()
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
def tiktok_liking_refresh():
     while True:

        tiktokClickThrough_REFRESHED2()
        time.sleep(3)
        p.click(93, 61)
        time.sleep(3)
#tiktok()
tiktok_liking()
#tiktok_liking_refresh()