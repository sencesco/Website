from selenium  import webdriver
from selenium.webdriver.common.by import By     # For import by to select the html element or by CSS selector
import pprint


# Keep Chrome browser opern after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Not frget to define options=chrome_options fo keep Chrome open
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org/")

search_bar = driver.find_element(By.NAME, "q")
# print(search_bar)   # Return : <selenium.webdriver.remote.webelement.WebElement (session="8dc740e851c7c1cb36234073e953385a", 
                      #           element="C9A21EFC987748032FF9A286E77E5252_element_5")> This meain can not print this element

# Specific a tag name element                    
print(f"Searchbar:\n{search_bar.tag_name}")
# Specific an attribute name
print(search_bar.get_attribute("placeholder"))  ;print()

button_go = driver.find_element(By.ID, "submit") 
print(f"Button go:\n{button_go.tag_name}")
print(button_go.text)
# Get size of button of button_go
print(button_go.size)   ;print()

doc_python_link = driver.find_element(By.CSS_SELECTOR, ".documentation-widget a")
print(f"documnet  python link:\n{doc_python_link.text}\n")

"""
  And this is done even though the actual link  doesn't have any easily identifiable name or class or ID.
On a similar way, sometimes it's extremely hard to even find an element even by CSS selector.
So if all else fails, one that will always work is the XPath. The Xpath look to similar way of file path
and use to specific path of html file.
  See more XPath detail: https://www.w3schools.com/xml/xpath_intro.asp

"""

# Can find by XPath wecan copy path from Chrome >> inspect >> choose element and right click copy >> copy XPath
download_xpath = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[1]/div[2]/h2')
print(f"downloadXPathn:\n{download_xpath.text}")
print(download_xpath.tag_name)  ;print()

# By this find element will select a first element if have multiple element
event_times = driver.find_element(By.CSS_SELECTOR, ".event-widget time")
print(f"Finde first element if  have multiple element: {event_times.text}\n")

# Find multiple element and return as a list
# old version of selenium can use find_element_by_css_selector but now they already cancel it.
event_times_list = driver.find_elements(By.CSS_SELECTOR,".event-widget time")
# The selenum not method to print list so will loop through a list and print text one by one
print("Finde all multiple element and loop through a list and print text one by one")
for times in event_times_list:
  print(times.text)
  
event_name = driver.find_elements(By.CSS_SELECTOR,".event-widget li a")

event_list = { f"Event No.{n}": {event_times_list[n].text: event_name[n].text} for n in range(len(event_times_list))}
pprint.pprint(event_list) 

driver.quit() # Closed all entired the browser
