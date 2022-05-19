import pandas as pd
import re
import itertools 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv
# form seleniumbase import seleniumbase

load_dotenv()


def launchBrowser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.linkedin.com/")
    return driver


browser = launchBrowser()
LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')

username = browser.find_element(By.ID, "session_key")
password = browser.find_element(By.ID, "session_password")
username.send_keys("mohitkumar11725@gmail.com")
password.send_keys(LINKEDIN_PASSWORD)
login = browser.find_element(By.CLASS_NAME, "sign-in-form__submit-button")
login.click()
browser.get("https://www.linkedin.com/jobs/")
job_title=browser.find_element(By.CLASS_NAME, "job-card-list__title")
company= browser.find_element(By.XPATH, "//span[@class='job-card-container__primary-description']//following-sibling::a")
location=browser.find_element(By.CLASS_NAME, "job-card-container__metadata-item")
job_links=browser.find_element(By.CLASS_NAME, "job-card-container__link")
c=[]
print(job_title.text)
for i in job_title:
    #print(i.text)
    c.append(i.text)
    # c.append(i.text.get_attribute("href"))

print(c,"\n")
print()
print(len(c))

