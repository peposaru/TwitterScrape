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
from selenium.webdriver.support.ui import Select


from bs4 import BeautifulSoup

baseUrl = 'https://x.com/'
hashtag = 'lang:en #nvidia'
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
tweets = 0
while tweets < tweetsTarget:
        scrollPauseTime = 1
        while True:
            last_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(scrollPauseTime)
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
            print('SCROLLED TO BOTTOM...')
            currentUrl = driver.page_source
            soup = BeautifulSoup(currentUrl, 'html.parser')
            for element in soup.find_all(attrs={"data-testid": "tweet"}):
                if element.find('span', string='Ad', style='text-overflow: unset;'):
                    print ('SKIPPING AD...')
                    continue

# Tweet Data
            username    = 
            handle      = 
            timeStamp   = 
            verified    =
            content     = 
            comments    = 
            retweets    = 
            likes       = 
            analytics   = 
            tags        = 
            mentions    = 
            emojis      = 
            tweetLink   = 
            tweetID     = 
    
# Person who posted it data
            tweeterID = 
            following = 
            follwers  = 

                tweetTextElement = element.find(attrs={"data-testid": "tweetText"})
                print (tweetTextElement.text)
                print ('----------------------------------------------------------------------------------')
                tweets+=1


        # df = pd.DataFrame(data)

        # current_time = now.strftime("%Y-%m-%d_%H-%M-%S")
        # file_path = f"{folder_path}{current_time}_tweets_1-{len(self.data)}.csv"
        # df.to_csv(file_path, index=False, encoding="utf-8")


