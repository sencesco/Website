from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# DRIVER_PATH = "./chromedriver.exe"  foruse local chrome webdriver 
# SHould match with chrome browser version problem now I use local but the speedtest.net need to use local driver
# So now (Sep 2023) chrome brroser ver sion is 116 vut webdrive not release yet that when use 
# self.driver = webdriver.Chrome() with not local path the speedtest.net can not go to thier page
# So Use other web site instead
""" class InternetSpeedTwitterBot:
  def __init__(self,driver_path):
    self.chrome_driver_path = driver_path
    self.chrome_options = webdriver.ChromeOptions()
    self.chrome_options.add_experimental_option("detach", True)
    self.service = ChromeService(executable_path=driver_path)
    self.driver = webdriver.Chrome(service=self.service,  options=self.chrome_options)
    self.up = 0
    self.down = 0
      
  def speed_test(self):
    self.driver.get("https://www.speedtest.net/") """


USR = "Twitter user"
PASS = "Twitter pass"
PROMISED_DOWN = 300
PROMISED_UP = 300
PROVIDER = "PlanetFiber"

class InternetSpeedTwitterBot:
  def __init__(self):
    self.chrome_options = webdriver.ChromeOptions()
    self.chrome_options.add_experimental_option("detach", True)
    self.driver = webdriver.Chrome(options=self.chrome_options)
    self.upload = 0
    self.download = 0
      
  def speed_test(self):
    self.driver.get("https://fast.com/#")
    time.sleep(30)
    press_show_more = self.driver.find_element(By.ID, "show-more-details-link")
    press_show_more.click()
    self.upload = self.driver.find_element(By.ID, "up-mb-value")
    self.download = self.driver.find_element(By.ID, "down-mb-value")
    print(self.upload.text, self.download.text)
    # self.driver.quit()

  def tweet_net_status(self):
    self.driver.get("https://twitter.com/i/flow/login")
    time.sleep(5)
    fill_usr = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    fill_usr.send_keys(USR)
    fill_usr.send_keys(Keys.ENTER)
    time.sleep(5)
    fill_pass = self.driver.find_element(By.NAME,"password")
    fill_pass.send_keys(PASS)
    fill_pass.send_keys(Keys.ENTER)
    time.sleep(5)
    tweet_compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
    tweet = f"Hey Internet Provider is #{PROVIDER}, why is my internet speed {self.download}MB(download)/{self.upload}MB(upload) when I pay for {PROMISED_DOWN}MB(down)/{PROMISED_UP}MB(up)?"
    tweet_compose.send_keys(tweet)
    time.sleep(5)
    tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
    tweet_button.click()
    time.sleep(5)
    self.driver.quit()

 #  ______________________ The code element will  alway update so check element locate again berfore run this code_____________________   
    
autorun = InternetSpeedTwitterBot() 
autorun.speed_test()
autorun.tweet_net_status()
