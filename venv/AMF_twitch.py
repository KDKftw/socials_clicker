import pyautogui as p
import time


def twitchFollowClose():
    time.sleep(16)
    p.click(588, 625)
    time.sleep(7)
    p.click(786, 16)
    time.sleep(13)

def tiktokClickThrough_REFRESHED2():
    time.sleep(4)
    p.click(682, 438)
    twitchFollowClose()

def twitch_flw():
    tiktokClickThrough_REFRESHED2()
    resetCounter = 0
    while True:
        time.sleep(4)
        p.click(684, 489)
        twitchFollowClose()
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

twitch_flw()