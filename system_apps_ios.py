import time
from appium import webdriver

APPIUM = "http://localhost:4723"
CAPS = {
    "platformName": "iOS",
    "appium:options": {
        "platformVersion": "17.0",
        "deviceName": "iPhone 15 Pro",
        "automationName": "XCUITest",
        "app": "com.apple.Preferences"
    }
}
driver = webdriver.Remote(APPIUM, CAPS)
try:
    time.sleep(5)   # for demo only -  to observe the app launch
    print(driver.page_source)
finally:
    if driver is not None:
        driver.quit()
