from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from dotenv import load_dotenv
import os
from time import sleep

class Bot:
    def __init__(self):
        load_dotenv('.env')
        self.chrome_driver_path = os.getenv('CHROME_PATH')
        self.twitter_username = os.getenv('TWITTER_USERNAME')
        self.twitter_pass = os.getenv('TWITTER_PASSWORD')
        service = Service(self.chrome_driver_path)
        self.driver = webdriver.Chrome(service=service)



    def get_speed(self):
        self.driver.get(url='https://www.speedtest.net/')
        go = self.driver.find_element(By.CLASS_NAME, 'start-text')
        go.click()
        while True:
            try:
                internet = self.driver.find_elements(By.CSS_SELECTOR, 'span.result-data-large.number.result-data-value')
                float(internet[2].text)
                break
            except ValueError:
                sleep(3)
                continue
        ping = 0
        download = 0
        upload = 0
        speed = [ping, download, upload]
        for i in range(len(internet)):
            speed[i] = internet[i].text
        speeds = f'ping: {speed[0]}\ndownload: {speed[1]}\nupload: {speed[2]}'
        return speeds

    def send_tweet(self, speeds: str):
        self.driver.get(url='https://twitter.com/')
        sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a/div/span/span')
        sign_in.click()
        sleep(2)
        username = self.driver.find_element(By.CSS_SELECTOR, 'input.r-30o5oe')
        username.click()
        username.send_keys(self.twitter_username)
        sleep(1)
        next = self.driver.find_element(By.CSS_SELECTOR, 'div.css-901oao.r-1awozwy.r-jwli3a')
        next.click()
        sleep(1)

        password = self.driver.find_element(By.NAME, 'password')
        password.click()
        password.send_keys(self.twitter_pass)
        login = self.driver.find_element(By.CSS_SELECTOR, 'div.css-901oao.r-1awozwy.r-jwli3a')
        login.click()
        sleep(2)
        tweet = self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div')
        tweet.click()
        sleep(2)

        tweet.send_keys(speeds)

        send_tweet = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
        send_tweet.click()

