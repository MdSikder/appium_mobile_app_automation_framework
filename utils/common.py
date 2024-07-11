import os
import time


def take_screenshot(driver, test_name):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_name = f"{test_name}_{timestamp}.png"
    screenshot_path = os.path.join("screenshots", screenshot_name)
    driver.save_screenshot(screenshot_path)
