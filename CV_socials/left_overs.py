import cv2
import time
import pyautogui as p
## https://docs.opencv.org/3.4/de/da9/tutorial_template_matching.html
#time.sleep(5)
##take screen on initial page, save, find view, get location, click
#myScreenshot = p.screenshot()
#myScreenshot.save('findView.png')
screenshot = cv2.imread("findView2.png", 1)
#template = cv2.imread("view_5_try.png", 6)
template = cv2.imread("view4.png", 6)
#res = cv2.matchTemplate(screenshot, template, cv2.TM_SQDIFF)        ##(-7.275957614183426e-12, 1.0, (656, 467), (15, 151))
res = cv2.matchTemplate(screenshot, template, cv2.TM_SQDIFF)
cv2.normalize( res, res, 0, 1, cv2.NORM_MINMAX, -1 )

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
print(res)
#print(cv2.minMaxLoc(res))
match_method = 3
result = cv2.matchTemplate(screenshot, template, match_method)
#print(result)


#min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
viewLocator = min_loc
match_loc = min_loc



#print(match_loc)

#print(viewLocator)
#
#print(min_val)
time.sleep(2)
#p.click(viewLocator)