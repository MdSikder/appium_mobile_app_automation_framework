import os
from appium import webdriver
from config import config


def get_driver():
    desired_caps = {
        "platformName": config.PLATFORM_NAME,
        "deviceName": os.getenv("DEVICE_NAME", config.DEVICE_NAME),
        "appPackage": os.getenv("APP_PACKAGE", config.APP_PACKAGE),
        "appActivity": os.getenv("APP_ACTIVITY", config.APP_ACTIVITY),
    }
    return webdriver.Remote(os.getenv("APPIUM_SERVER_URL", config.APPIUM_SERVER_URL), desired_caps)
