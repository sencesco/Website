from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import *

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")

fill_name = driver.find_element(By.NAME, "fName")
fill_name.send_keys("Yorname")
fill_name.send_keys(Keys.TAB)
fill_surname = driver.find_element(By.NAME, "lName")
fill_surname.send_keys("Yoursurname")
fill_surname.send_keys(Keys.TAB)
fill_email = driver.find_element(By.NAME, "email")
fill_email.send_keys("Yourmail@gmail.com")
fill_email.send_keys(Keys.TAB)
click_submit = driver.find_element(By.CSS_SELECTOR, "button")
click_submit.click()
