import time
from appium import webdriver

APPIUM = "http://localhost:4723"
CAPS = {
    "platformName": "Android",
    "appium:options": {
        "platformVersion": "13.0",
        "deviceName": "Android Emulator",
        "automationName": "UiAutomator2",
        "appPackage": "com.android.settings",
        "appActivity": ".Settings"
    }
}
driver = webdriver.Remote(APPIUM, CAPS)
try:
    time.sleep(5)   # for demo only -  to observe the app launch
    print(driver.page_source)
finally:
    if driver is not None:
        driver.quit()
