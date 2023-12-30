import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "Yourmail@gmail.com"
password = "YourApp_pass"

amazon_url = "https://www.amazon.com/ASUS-Vivobook-Display-GeForce%C2%AE-M6500XV-EB96/dp/B0C7RNP65K/ref=sr_1_3?keywords=laptop+ryzen+9&sr=8-3"
# Check your HTTP header info.: https://myhttpheader.com/
header = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
  "Accept-Language": "en-US,en;q=0.5"
}

response = requests.get(amazon_url, headers=header)   # Some web site if we not prefix a header will get an infomation some part not all of this page
amazon_nb_page = response.text

soup = BeautifulSoup(amazon_nb_page, "html.parser")

#                                                                  spilt output frrom $1,234  delete "," and convert to a float 
nb_price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1].replace(",", ""))
print(nb_price)

nb_title = soup.find(name="span",id="productTitle").getText()
print(nb_title)

email_subject = "ASUS Vivobook Pro 15 Laptop(Ryzen 9) Price in target"
add_content = "The price has reach below $1000, now is on sale = $"

if nb_price < 1000:
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
      from_addr= my_email, 
      to_addrs= "Yourmail or receiver@gmail.com", 
      msg= 'Subject: {}\n\n{}. {}{}'.format(email_subject, nb_title.encode("utf-8"), add_content, nb_price)
      )
