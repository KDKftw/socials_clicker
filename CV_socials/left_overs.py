time.sleep(5)
##take screen on initial page, save, find view, get location, click
myScreenshot = p.screenshot()
myScreenshot.save('findView.png')
screenshot = cv2.imread("findView.png", 0)
template = cv2.imread("view4.png", 0)
res = cv2.matchTemplate(screenshot, template, cv2.TM_SQDIFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
viewLocator = min_loc

print(viewLocator)
print(cv2.minMaxLoc(res))
time.sleep(2)
p.click(viewLocator)