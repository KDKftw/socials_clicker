import pyautogui as p
import time

def twiter_follow_click_close():
    time.sleep(11)
    p.click(308, 297)
    time.sleep(6)
    p.click(575, 14)
    time.sleep(6)

def twitterClickThrough_REFRESHED():
    time.sleep(3)
    p.click(676, 506)
    twiter_follow_click_close()
    p.click(672, 508)
    time.sleep(6)

def twitter():
    twitterClickThrough_REFRESHED()
    resetCounter = 0
    doluSmernice = 599

    while True:
        time.sleep(3)
        p.click(681, doluSmernice)
        twiter_follow_click_close()
        p.click(681, doluSmernice)
        resetCounter = resetCounter + 1
        print(resetCounter)
        time.sleep(6)

        if resetCounter == 2:
            p.click(76, 59)
            time.sleep(4)
            twitterClickThrough_REFRESHED()
            resetCounter = 0
        else:
            pass


def twitter_retweet_close():
    time.sleep(11)
    p.click(309, 426)    ##retwet
    time.sleep(6)
    p.click(586, 12)
    time.sleep(3)
def twitterClickThrough_REFRESHED_RETWEET():
    time.sleep(3)
    p.click(676, 506)
    twitter_retweet_close()
    p.click(672, 508)
    time.sleep(6)

def twitter_retweeting():
        twitterClickThrough_REFRESHED_RETWEET()
        resetCounter = 0
        doluSmernice = 599
        while True:
            time.sleep(3)
            p.click(681, doluSmernice)
            twitter_retweet_close()
            p.click(681, doluSmernice)
            resetCounter = resetCounter + 1
            print(resetCounter)
            time.sleep(6)
            if resetCounter == 2:
                p.click(76, 59)
                time.sleep(4)
                twitterClickThrough_REFRESHED_RETWEET()
                resetCounter = 0
            else:
                pass

def twitter_retweet_close2():
    time.sleep(11)
    p.click(309, 426)    ##retwet
    time.sleep(6)
    p.click(484, 14)
    time.sleep(3)
def twitterClickThrough_REFRESHED_LIKING():
    time.sleep(3)
    p.click(676, 506)
    twitter_retweet_close2()
    p.click(672, 508)
    time.sleep(6)

def twitter_liking():
        twitterClickThrough_REFRESHED_LIKING()
        resetCounter = 0
        doluSmernice = 599
        while True:
            time.sleep(3)
            p.click(681, doluSmernice)
            twitter_retweet_close2()
            p.click(681, doluSmernice)
            resetCounter = resetCounter + 1
            print(resetCounter)
            time.sleep(6)
            if resetCounter == 2:
                p.click(76, 59)
                time.sleep(4)
                twitterClickThrough_REFRESHED_LIKING()
                resetCounter = 0
            else:
                pass
twitter()
#twitter_retweeting()
#twitter_liking()