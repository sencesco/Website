from bs4 import BeautifulSoup

# "encoding="utf8"" for decode some character that can not decode
with open("website.html", encoding="utf8") as file:
  content = file.read()
  
soup = BeautifulSoup(content, "html.parser")

"""
print(soup) >> will output the whole html code without identation of the code
"""
# With prettify() method in bs4 will show a html code with identation
print(soup.prettify())
print()

# Print first <a> element
print(soup.a)
print()

# Print first <li> element
print(soup.li)
print()

# find_all() method in bs4 will find all specific element and show as the list
find_all_element = soup.find_all(name="a")
print(find_all_element)
print()

# For can see all element from list
for tag in find_all_element:
  print(tag)
print()
  
for tag in find_all_element:
  print(tag.get("href"))  # For can get a value of specific attribute in tag
print()

# find() method in bs4 will find only specific tag with attribute or class
h1_id_name = soup.find(name="h1", id="name")
print(h1_id_name)
print()

# In case if find a specific class will return only a first tag element
# class__ need specify this becuase in Python it's a reserved keyword
# If not do like this, wil get Error
h3_class_heading = soup.find(name="h3", class_="heading")
print(h3_class_heading)
print()
  
# Print tag name  
print(h3_class_heading.name)
print()

# Print text is contian in h3
print(h3_class_heading.getText())
print()

# Print a Class name
print(h3_class_heading.get("class"))
print()

# _____________ We can use CSS selector in bs4 module to find an element, 
# ____attribue and vice versa same as  how to use CSS selector in HTML_____

# With select_one will return only the first tag of specific CSS selector
name = soup.select_one("#name")   # Return id="name" in h1
print(name)

# find with CSS element selector
company_url = soup.select_one("p a")
print(company_url)
print()

# With select will return all of tag of specific CSS selector
heading = soup.select(".heading")
print(heading)