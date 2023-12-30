from selenium  import webdriver
from selenium.webdriver.common.by import By     # For import by to select the html element or by CSS selector


# Keep Chrome browser opern after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Not frget to define options=chrome_options fo keep Chrome open
driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://www.amazon.com")    # Open amazon website with Crome browser

#____Try it on day 47 project __________________
driver.get("https://www.amazon.com/ASUS-Vivobook-Display-GeForce%C2%AE-M6500XV-EB96/dp/B0C7RNP65K/ref=sr_1_3?keywords=laptop+ryzen+9&sr=8-3")

nb_price_dollar = driver.find_element(By.CLASS_NAME, "a-price-whole")
nb_price_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
print(f"The price is {nb_price_dollar.text}.{nb_price_cents.text}")

# driver.close() # Closed only particula tab
driver.quit() # Closed all entired the browser