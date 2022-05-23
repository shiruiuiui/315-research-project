import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time, os

from scrape import *

driverpath ='driver/chromedriver'

driver = webdriver.Chrome(driverpath)
driver.get('https://www.tiktok.com/')
action = ActionChains(driver)
#print(driver.title)
#sleep to give us time to do the captcha
time.sleep(10)
#must manually log into tiktok with one of 3 tiktok accounts (conservative/liberal/neutral) first
       
data = [{"data": []} for i in range(5) ]
# change to whichever account is logged in
scrape("conservative",driver,data)
#scrape("liberal")
#scrape("neutral")

