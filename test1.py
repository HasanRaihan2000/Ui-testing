from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.options import Options as chromeOptions
from selenium.webdriver.firefox.options import Options as fireFoxOptions
import time
import os

def main():
    devices = {
        "Desktop": {
            "1920x1080": (1920, 1080),
            "1366x768": (1366, 768),
            "1536x864": (1536, 864)
        },
        "Mobile": {
            "360x640": (360, 640),
            "414x896": (414, 896),
            "375x667": (375, 667)
        }
    }   

    browsers = ['chrome','firefox']
    
    for device_type, resolutions in devices.items():
        for resolution_name, resolution in resolutions.items():
            width, height = resolution

            for browser in browsers:
                if browser == 'chrome':
                    options = chromeOptions()
                    options.add_argument("--headless")
                    options.add_argument(f"--window-size={width},{height}")
                    driver = webdriver.Chrome(options=options)
                elif browser == 'firefox':
                    options = fireFoxOptions()
                    options.add_argument("--headless")
                    options.add_argument(f"--window-size={width},{height}")
                    driver = webdriver.Firefox(options=options)
                else:
                    print('something went wrong')
                    continue

                urls = [
                "https://www.getcalley.com/calley-lifetime-offer/",
                "https://www.getcalley.com/see-a-demo/",
                "https://www.getcalley.com/calley-teams-features/",
                "https://www.getcalley.com/calley-pro-features/",
                "https://www.getcalley.com/"
                ]

                for url in urls:
                    screenshotdir = os.path.join(browser, device_type, resolution_name)

                    timestamp = time.strftime("%Y%m%d-%H%M%S")
                    screenshot_file = os.path.join(screenshotdir, f"screenshot-{timestamp}.png")
                    os.makedirs(screenshotdir, exist_ok=True)
                    driver.get(url)


                    s = lambda x: driver.execute_script('return document.body.parentNode.scroll' + x)
                    driver.set_window_size(s('Width'), s('Height'))
                    ele = driver.find_element(By.TAG_NAME, 'body')

                    driver.implicitly_wait(10)
                    ele.screenshot(screenshot_file)
                    print(f"{browser}:{device_type}:{resolution_name}:{url} screenshot taken")
                    
                driver.quit()


main()
