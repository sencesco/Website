from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys   # For can pressthe enter on search box after key text

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article_count = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
print(article_count.text)

# Will auto click this elemnt and already go to the page of this link with mousr position near the link
"""
article_count.click()
"""
# Method By.LINK_TEXT will search link name with text name of the link
click_link_Content_portals  = driver.find_element(By.LINK_TEXT, "Content portals")
click_link_Content_portals.click()

# Input text and enter in input bar
input_text_search = driver.find_element(By.CLASS_NAME, "searchboxInput")
input_text_search.send_keys("Python")
input_text_search.send_keys(Keys.ENTER)

