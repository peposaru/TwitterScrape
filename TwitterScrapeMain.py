import pandas as pd
import os
import time
import json
import requests
from inspect import currentframe, getframeinfo


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ChromeOptions, Keys

from bs4 import BeautifulSoup

baseUrl = 'https://x.com/'
hashtag = '#nvidia'
tweetsTarget = 10

cf = currentframe()
filename = getframeinfo(cf).filename
os.chdir(r'C:\Users\keena\Desktop\Nvidia Project\Twitter')
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

accountInfo = 'TwitterCredentials.json'
with open (accountInfo,'r') as credFile:
    jsonData = json.load(credFile)
    username = jsonData['userName']
    password      = jsonData['pwd']

options = ChromeOptions()
options.add_argument("--start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(options=options)

# Open the Twitter login page
url = "https://twitter.com/i/flow/login"
driver.get(url)

# Find and input the username
username_input = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[autocomplete="username"]')))
username_input.send_keys(username)
username_input.send_keys(Keys.ENTER)

# Find and input the password
password_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="password"]')))
password_input.send_keys(password)
password_input.send_keys(Keys.ENTER)

# Checking to see if search bar is present
try:
    searchElementPresent = EC.presence_of_element_located((By.CSS_SELECTOR, 'input[data-testid="SearchBox_Search_Input"]'))
    WebDriverWait(driver, 10).until(searchElementPresent)
    print ('SEARCH BOX PRESENT...')
except:
    print (f'ERROR...CODE LINE {cf.f_lineno}')
    print('ENDING SEQUENCE...')
    driver.quit()
    quit()

# Inputting Hashtag
try:
    searchInput = driver.find_element(By.CSS_SELECTOR,'input[data-testid="SearchBox_Search_Input"]')
    searchInput.click()
    searchInput.send_keys(hashtag)
    searchInput.send_keys(Keys.RETURN)
except:
    print (f'ERROR...CODE LINE {cf.f_lineno}')
    print('ENDING SEQUENCE...')
    driver.quit()
    quit()

# Switching to Latest Tab
try:
    lastestTabElement = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@role='tab']//span[text()='Latest']")))    
    lastestTabElement.click()
except:
    print (f'ERROR...CODE LINE {cf.f_lineno}')
    print('ENDING SEQUENCE...')
    driver.quit()
    quit()

# Scrolling down infinite scroll
while True:
    try:
        scrollPauseTime = 1
        while True:
            last_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scrollPauseTime)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            print('SCROLLED TO BOTTOM')
            currentUrl = driver.current_url
            response = requests.get(currentUrl)
            soup = BeautifulSoup(response.content, 'html.parser')
            tweets = soup.find_all('div',class_= "css-175oi2r")
            print (tweets)
            for tweet in tweets:
                print(tweet)
    except:
        print('SCROLL FAILED...')
        print (f'ERROR...CODE LINE {cf.f_lineno}')
        print('ENDING SEQUENCE...')
        quit()
    # try: 
    #     currentUrl = driver.current_url
    #     response = requests.get(currentUrl)
    #     soup = BeautifulSoup(response.content, 'html.parser')
    #     for tweet in soup.find_all('div', class_="css-175oi2r"):
    #         print(tweet)
    # except:
    #     print('TWEET SCRAPE FAILED...')
    #     print (f'ERROR...CODE LINE {cf.f_lineno}')
    #     print('ENDING SEQUENCE...')
    #     quit() 





        # def save_to_csv(self):
        # print("Saving Tweets to CSV...")
        # now = datetime.now()
        # folder_path = "./tweets/"

        # if not os.path.exists(folder_path):
        #     os.makedirs(folder_path)
        #     print("Created Folder: {}".format(folder_path))

        # data = {
        #     "Name": [tweet[0] for tweet in self.data],
        #     "Handle": [tweet[1] for tweet in self.data],
        #     "Timestamp": [tweet[2] for tweet in self.data],
        #     "Verified": [tweet[3] for tweet in self.data],
        #     "Content": [tweet[4] for tweet in self.data],
        #     "Comments": [tweet[5] for tweet in self.data],
        #     "Retweets": [tweet[6] for tweet in self.data],
        #     "Likes": [tweet[7] for tweet in self.data],
        #     "Analytics": [tweet[8] for tweet in self.data],
        #     "Tags": [tweet[9] for tweet in self.data],
        #     "Mentions": [tweet[10] for tweet in self.data],
        #     "Emojis": [tweet[11] for tweet in self.data],
        #     "Profile Image": [tweet[12] for tweet in self.data],
        #     "Tweet Link": [tweet[13] for tweet in self.data],
        #     "Tweet ID": [f'tweet_id:{tweet[14]}' for tweet in self.data],
        # }

        # if self.scraper_details["poster_details"]:
        #     data["Tweeter ID"] = [f'user_id:{tweet[15]}' for tweet in self.data]
        #     data["Following"] = [tweet[16] for tweet in self.data]
        #     data["Followers"] = [tweet[17] for tweet in self.data]

        # df = pd.DataFrame(data)

        # current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        # file_path = f"{folder_path}{current_time}_tweets_1-{len(self.data)}.csv"
        # pd.set_option("display.max_colwidth", None)
        # df.to_csv(file_path, index=False, encoding="utf-8")

        # print("CSV Saved: {}".format(file_path))

        # pass
