from time import sleep
import time, os
from tags import *
def engage_video(acct,tags,video,driver):
    """
    Given an account (either liberal, conservative or neutral) engage_video determines if the bot will engage with a post based on hastags used.
    If a video meets "engage criteria", engage_video will watch the video for 3 minutes.
    """
    like = driver.find_element_by_xpath("//*[@id=\"app\"]/div[2]/div[2]/div[1]/div[1]/div/div[2]/div[2]/button[1]/span")
    exist = []
    for t in tags:
        print(t)
        if(t in conservative_tags and acct == "conservative"):
            time.sleep(180)
            exist.append(1)
        elif(t in liberal_tags and acct == "liberal"):
            time.sleep(180)
            exist.append(1)
        elif((t in neutral_tags) and acct == "neutral"):
            time.sleep(180)
            exist.append(1)
        else:
            exist.append(-1)
    if 1 in exist:
        return 1
    else:
        return -1

