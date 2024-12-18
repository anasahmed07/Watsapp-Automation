from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_profile_path = "user-data-dir=C:\\Users\\M.A COM\\AppData\\Local\\Google\\Chrome\\User Data\\WatsappAutomation"
options = webdriver.ChromeOptions()
options.add_argument(chrome_profile_path)
browser=webdriver.Chrome(options=options)

while(True):
    print("Starting Automation...")
    browser.get("https://www.instagram.com/")
    wait = WebDriverWait(browser,300)
    time.sleep(500)