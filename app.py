import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def launchBrowser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.linkedin.com")
    return driver


browser = launchBrowser()

username = browser.find_element(By.ID, "session_key")
password = browser.find_element(By.ID, "session_password")
username.send_keys("mohitkumar11725@gmail.com")
password.send_keys(LINKEDIN_PASSWORD)
login = browser.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
login.click()
driver.get("https://www.linkedin.com/jobs/")
