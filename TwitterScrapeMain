# Scraping Twitter in order to do a sentiment analysis

import pandas as pd 
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os,time,json,requests
from bs4 import BeautifulSoup

from selenium.webdriver import ChromeOptions, Keys

class TwitterAccount:
    def login_twitter(self,username: str, password: str) -> None:
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

        # Wait for a short period (e.g., 10 seconds) to ensure the login process completes
        time.sleep(10)


# Scrape Page
class TwitterScraper:

    def readPage(self,url):
        response = requests.get(url)
        soup     = BeautifulSoup(response.content, 'html.parser')
        return soup

    # def tweetScrape(self):
    #     user      = 
    #     hashtags  = 
    #     links     = 
    #     tweet     = 
    #     poll      = 
    #     replies   = 
    #     reposts   = 
    #     likes     = 
    #     views     = 
    #     timeStamp = 

# Put into Pandas Spreadsheet
# class PandasManager:
#     def __init__(self):
#         asdfs

# Handles Printing Messages
class Printing:
    def __init__(self):
        adfasd

# Main Process
if __name__ == "__main__":

    directory =  r'C:\Users\keena\Desktop\Nvidia Project\Twitter'
    os.chdir(directory)      

    # Selenium
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Twitter Account Info
    accountInfo = 'TwitterCredentials.json'
    with open (accountInfo,'r') as credFile:
        jsonData = json.load(credFile)
        userName = jsonData['userName']
        pwd      = jsonData['pwd']
    
    # Site and Desired Hashtag
    baseUrl = 'https://x.com/'
    hashtag = '#nvidia'


    twitterAccount = TwitterAccount()
    twitterScraper = TwitterScraper()    
    # pandasManager  = PandasManager()
    # prints         = Printing()

    twitterAccount.login_twitter(userName,pwd)

    while True:
        soup = twitterScraper.readPage(baseUrl)
        for tweet in soup.find_all('div', class_="css-175oi2r"):
            print (tweet)
            time.sleep(5)
