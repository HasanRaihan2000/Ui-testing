# Ui-testing

## Webpage Screenshot Automation

## Overview

This project automates the process of capturing screenshots of specified web pages across different devices and resolutions using Selenium WebDriver. The script supports both Chrome and Firefox browsers and runs in headless mode to take screenshots without opening the browser window.

## Features

- **Multi-browser support**: Works with Chrome and Firefox.
- **Device Emulation**: Supports both desktop and mobile device resolutions.
- **Headless Browsing**: Runs browsers in headless mode to capture screenshots without a visible UI.
- **Automated Screenshot Saving**: Captures screenshots of specified URLs and saves them in a structured directory format.

## Installation

1. **Clone the repository**:
   
   ```bash
   git clone https://github.com/HasanRaihan2000/Ui-testing.git
   cd Ui-testing
   ```
2. **Install the required Python packages:**:
   
   ```
   pip install selenium
   ```
3. **Download WebDriver executables**:

   - ChromeDriver for Chrome
   - GeckoDriver for Firefox
  
     Ensure that the downloaded drivers are in your system's PATH or place them in the project directory.

4. **Run the script**:

   ```
   python test1.py
   ```
   The script will take screenshots of the specified URLs for each device resolution and browser    combination.

5. **Check the screenshots**:
   Screenshots will be saved in the following directory structure:
  ## Directory Structure

This project contains screenshot files organized by browser, device type, and screen resolution.

### Screenshot Directory

* **chrome/**: Contains screenshots taken with Chrome.
  * **Desktop/**: Contains screenshots taken on desktop devices.
    * **1920x1080/**: Contains screenshots with a resolution of 1920x1080 pixels.
    * **1366x768/**: Contains screenshots with a resolution of 1366x768 pixels.
  * **Mobile/**: Contains screenshots taken on mobile devices.
    * **360x640/**: Contains screenshots with a resolution of 360x640 pixels.
* **firefox/**: Contains screenshots taken with Firefox.
  * **Desktop/**: Contains screenshots taken on desktop devices.
    * **1920x1080/**: Contains screenshots with a resolution of 1920x1080 pixels.
  * **Mobile/**: Contains screenshots taken on mobile devices.
    * **360x640/**: Contains screenshots with a resolution of 360x640 pixels.
