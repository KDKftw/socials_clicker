import cv2
import time
import pyautogui as p
#viewLocator = max_loc
##default browser = edge
##template to find to_name == the picture im looking for in the screenshot of the display, gotta be pre-set


##cv2.IMREAD_COLOR: It specifies to load a color image. Any transparency of image will be neglected. It is the default flag.
# Alternatively, we can pass integer value 1 for this flag.
##second parameter of imread method
def takeSS_findTemplateInScreen_clickOnTemplate(screenShotOfDisplay_name, templateToFindTo_name):

    ##take screen on initial page, save, find view, get location, click
    myScreenshot = p.screenshot()
    myScreenshot.save(screenShotOfDisplay_name+".png")
    screenshot = cv2.imread(screenShotOfDisplay_name+".png", 1)##scnd value=0
    template = cv2.imread(templateToFindTo_name+".png",  1)####scnd value=0
    res = cv2.matchTemplate(screenshot, template, cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    viewLocator = min_loc

    print(viewLocator)
    #print(cv2.minMaxLoc(res))
    time.sleep(2)
    p.click(viewLocator)


def ytbe_like():
    resetCounter = 0
    while True:
        time.sleep(5)
        takeSS_findTemplateInScreen_clickOnTemplate("screenshot_step1", "view4")
        time.sleep(3)
        takeSS_findTemplateInScreen_clickOnTemplate("screenshot_step2", "maximize_window")
        time.sleep(6)
        p.click(18, 450)
        time.sleep(1)
        p.press("down", presses=3)
        time.sleep(3)
        time.sleep(3)
        takeSS_findTemplateInScreen_clickOnTemplate("screenshot_step3", "thumbsUP")
        time.sleep(8)
        takeSS_findTemplateInScreen_clickOnTemplate("screenshot_step4", "crossClose2")
        time.sleep(10)
        if resetCounter == 4:
            takeSS_findTemplateInScreen_clickOnTemplate("screenshot_step5", "load_more")
            resetCounter = 0
            time.sleep(7)
        else:
            pass

def pinterest_flw():
    resetCounter = 0
    while True:
        time.sleep(5)
        takeSS_findTemplateInScreen_clickOnTemplate("screenshot_step1", "view4")
        time.sleep(6)
        takeSS_findTemplateInScreen_clickOnTemplate("screenshot_step2", "maximize_window")
        time.sleep(4)
        takeSS_findTemplateInScreen_clickOnTemplate("screenshot_step3", "follow_pinterest")
        time.sleep(8)
        takeSS_findTemplateInScreen_clickOnTemplate("screenshot_step4", "crossClose2")
        time.sleep(10)
        resetCounter = resetCounter+1

        if resetCounter==4:
            takeSS_findTemplateInScreen_clickOnTemplate("screenshot_step5", "load_more")
            resetCounter=0
        else:
            pass

def ytbe_sub():
    resetCounter=0
    while True:
        time.sleep(7)
        takeSS_findTemplateInScreen_clickOnTemplate("screenshot_step1", "view4")
        time.sleep(7)
        takeSS_findTemplateInScreen_clickOnTemplate("screenshot_step2", "maximize_window")
        time.sleep(7)
        takeSS_findTemplateInScreen_clickOnTemplate("screenshot_step3", "sub_ytbe")
        time.sleep(8)
        takeSS_findTemplateInScreen_clickOnTemplate("screenshot_step4", "crossClose2")
        time.sleep(10)

        resetCounter = resetCounter + 1

        if resetCounter == 3:
            takeSS_findTemplateInScreen_clickOnTemplate("screenshot_step5", "load_more")
            resetCounter = 0
            time.sleep(10)
        else:
            pass


#ytbe_like()
#pinterest_flw()
ytbe_sub()