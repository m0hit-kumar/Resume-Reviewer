import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


def launchBrowser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.linkedin.com")
    return driver


browser = launchBrowser()

username = browser.find_element_by_id("session_key")
password = browser.find_element_by_id("session_password")
