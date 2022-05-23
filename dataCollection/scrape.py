
from bs4 import BeautifulSoup
import requests

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

from extract_hastags import extract_hashtags
from tags import *
from engage import engage_video


def get_page(driver):
    return driver.find_element_by_tag_name("html")

def scrape(acct,driver, data):
    scrollCount, currentVid, s1count, s2count, s3count, s4count, s5count = 0, 0, 0, 0, 0, 0, 0
    captions = []
    engagement_count = 0
    stage = "s1"
    
    # allow time for video to auto-play
    time.sleep(1)

    # set engagement_count to -1 to break loop
    while(engagement_count >= 0):
        # allow time for video to auto-play
        time.sleep(4)
        print("scroll: "+ str(scrollCount))
        print("engage: "+ str(engagement_count))

        #refresh page after 100 scrolls
        if (currentVid == 100):
            driver.refresh()
            currentVid = 0
            # allow time for video to auto-play
            time.sleep(5)
        
        # update loaded html
        soup = BeautifulSoup(driver.page_source,'html.parser')
        
        video = soup.find('video')
        caption = video.parent.parent.parent.parent.parent.parent.text
        tags = extract_hashtags(caption)
        link = soup.find('video')['src']
        engage = engage_video(acct,tags,soup.find('video'),driver)
        print("tags: " + str(tags))

        if(engage == 1):
            engagement_count += 1
        
        #stage 1 (0-10)
        if(engagement_count < 11 and stage == "s1"):
            print("stage1")
            data[0]['data'].append((caption, tags, link, engage))
            data[0]['stats'] = (scrollCount, engagement_count)
            # update
            if(engagement_count == 10):
                s1count = scrollCount
                stage = "s2"

        #stage 2 (10-20)
        elif(engagement_count < 21 and stage == "s2"):
            print("stage2")
            data[1]['data'].append((caption,tags,link, engage))
            data[1]['stats'] = (scrollCount - s1count, engagement_count)
            # update
            if(engagement_count == 20):
                s2count = scrollCount - s1count
                stage = "s3"

        #stage 3 (20-30)
        elif(engagement_count < 31 and stage == "s3"):
            print("stage3")
            data[2]['data'].append((caption,tags,link, engage))
            data[2]['stats'] = (scrollCount - s2count, engagement_count)
            # update
            if(engagement_count == 30):
                s3count = scrollCount - s2count
                stage = "s4"
        
        #stage 4 (30-40)
        elif(engagement_count < 41 and stage == "s4"):
            print("stage4")
            data[3]['data'].append((caption,tags,link, engage))
            data[3]['stats'] = (scrollCount - s3count, engagement_count)
            # update
            if(engagement_count == 40):
                s4count = scrollCount-s3count
                stage == "s5"
            
        #stage 5 (40-50)
        elif(engagement_count < 51 and stage == "s5"):
            print("stage5")
            data[4]['data'].append((caption,tags,link, engage))
            data[4]['stats'] = (scrollCount - s4count, engagement_count)
            # update
            if(engagement_count == 50):
                s5count = scrollCount-s4count
                stage = "end"
            
        # all stages are complete
        else:
            engagement_count = -1
            
        
        # scroll to next video and increase counter
        get_page().send_keys(Keys.DOWN)
        scrollCount += 1 
        currentVid += 1
